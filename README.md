# Fusion Typography Preset

DaVinci Resolve Edit 페이지에서 바로 쓸 수 있는 간단한 `rise + fade` 텍스트 타이틀 프리셋입니다.

## 포함 파일

- `package/Edit/Titles/Codex Rise Fade.setting`
- `package/Edit/Titles/Codex Rise Fade Pro.setting`
- `install.ps1`

## 동작

- 0프레임에서 텍스트가 아래 조건으로 시작합니다.
- 위쪽에서 올라오며 나타남
- 불투명도 0에서 100으로 상승
- 48프레임에 최종 위치와 최종 불투명도에 도달
- 이후에는 정지 상태 유지

## 설치

PowerShell에서 아래를 실행합니다.

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\install.ps1
```

설치 후 DaVinci Resolve를 재시작하거나 Effects Library를 새로고침하면 `Titles`에 아래 프리셋이 나타납니다.

- `Codex Rise Fade`
- `Codex Rise Fade Pro`

## 프리셋 차이

### Codex Rise Fade

가장 단순한 버전입니다.

- Text
- Font
- Style
- Size
- Position
- Tracking
- Color
- Character Stagger

### Codex Rise Fade Pro

조절 가능한 애니메이션 버전입니다.

- Text
- Font
- Style
- Size
- Position
- Tracking
- Color
- Animation Speed
- Ease In
- Ease Out
- X Offset
- Y Offset
- Fade Strength
- Character Stagger
- Motion Blur
- Quality
- Shutter Angle
- Intro Blur
- Outro Blur

## 참고

- 기본 `Codex Rise Fade`는 48프레임 기준의 고정형입니다.
- `Codex Rise Fade Pro`는 속도와 진입량을 직접 조절하는 버전입니다.
- `Intro Blur`는 시작할 때 흐렸다가 선명해지는 양입니다.
- `Outro Blur`는 끝부분에서 다시 흐려지는 양입니다.
- 텍스트 전체가 한 번에 움직이게 하려면 `Character Stagger`를 `0`으로 두면 됩니다.
