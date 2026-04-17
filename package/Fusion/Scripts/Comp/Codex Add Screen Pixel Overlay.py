import sys


def get_comp():
    try:
        return comp
    except NameError:
        sys.path.append(r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules")
        import DaVinciResolveScript as dvr

        resolve = dvr.scriptapp("Resolve")
        if not resolve:
            return None
        fusion = resolve.Fusion()
        if not fusion:
            return None
        return fusion.GetCurrentComp()


def main():
    current_comp = get_comp()
    if not current_comp:
        print("No active Fusion comp found.")
        return

    source = current_comp.ActiveTool
    if not source:
        print("Select the source node first.")
        return

    coverage = 1.25

    vrect = current_comp.AddTool("sRectangle")
    vgrid = current_comp.AddTool("sGrid")
    vrender = current_comp.AddTool("sRender")
    vxf = current_comp.AddTool("Transform")
    merge1 = current_comp.AddTool("Merge")

    hrect = current_comp.AddTool("sRectangle")
    hgrid = current_comp.AddTool("sGrid")
    hrender = current_comp.AddTool("sRender")
    hxf = current_comp.AddTool("Transform")
    merge2 = current_comp.AddTool("Merge")

    vrect.SetAttrs({"TOOLS_Name": "CodexScreenGridShape"})
    vgrid.SetAttrs({"TOOLS_Name": "CodexScreenGrid"})
    vrender.SetAttrs({"TOOLS_Name": "CodexScreenGridRender"})
    vxf.SetAttrs({"TOOLS_Name": "CodexScreenGridCoverage"})
    merge1.SetAttrs({"TOOLS_Name": "CodexScreenGridMerge"})
    hrect.SetAttrs({"TOOLS_Name": "CodexScanlineShape"})
    hgrid.SetAttrs({"TOOLS_Name": "CodexScanlineGrid"})
    hrender.SetAttrs({"TOOLS_Name": "CodexScanlineRender"})
    hxf.SetAttrs({"TOOLS_Name": "CodexScanlineCoverage"})
    merge2.SetAttrs({"TOOLS_Name": "CodexScreenPixelOverlay"})

    vrect.SetInput("Width", 0.0009)
    vrect.SetInput("Height", 1.0)
    vrect.SetInput("Red", 0.65)
    vrect.SetInput("Green", 0.95)
    vrect.SetInput("Blue", 1.0)
    vrect.SetInput("Alpha", 1.0)

    vgrid.SetInput("CellsX", int(320 * coverage))
    vgrid.SetInput("CellsY", 1)
    vgrid.SetInput("XOffset", 0.0031)
    vgrid.SetInput("YOffset", 0.0)
    vgrid.SetInput("Input", vrect)
    vrender.SetInput("Input", vgrid)
    vxf.SetInput("Input", vrender)
    vxf.SetInput("Size", coverage)

    merge1.SetInput("Background", source)
    merge1.SetInput("Foreground", vxf)
    merge1.SetInput("Blend", 0.55)

    hrect.SetInput("Width", 1.0)
    hrect.SetInput("Height", 0.0012)
    hrect.SetInput("Red", 0.0)
    hrect.SetInput("Green", 0.0)
    hrect.SetInput("Blue", 0.0)
    hrect.SetInput("Alpha", 1.0)

    hgrid.SetInput("CellsX", 1)
    hgrid.SetInput("CellsY", int(270 * coverage))
    hgrid.SetInput("XOffset", 0.0)
    hgrid.SetInput("YOffset", 0.0037)
    hgrid.SetInput("Input", hrect)
    hrender.SetInput("Input", hgrid)
    hxf.SetInput("Input", hrender)
    hxf.SetInput("Size", coverage)

    merge2.SetInput("Background", merge1)
    merge2.SetInput("Foreground", hxf)
    merge2.SetInput("Blend", 0.35)

    media_out = current_comp.FindTool("MediaOut1") or current_comp.FindTool("MediaOut")
    if media_out:
        media_out.SetInput("Input", merge2)

    try:
        current_comp.SetActiveTool(merge2)
    except Exception:
        pass

    print("Codex Screen Pixel Overlay inserted.")


if __name__ == "__main__":
    main()
