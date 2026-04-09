# Fusion Typography Preset

DaVinci Resolve Edit 페이지에서 바로 쓸 수 있는 간단한 `rise + fade` 텍스트 타이틀 프리셋입니다.

## 포함 파일

- `package/Edit/Titles/Codex Rise Fade.setting`
- `package/Edit/Titles/Codex Rise Fade Pro.setting`
- `package/Edit/Titles/Codex Rise Fade Pro Alt.setting`
- `package/Edit/Titles/Codex Mask Reveal Pro.setting`
- `package/Edit/Effects/Codex 3D Arc Image.setting`
- `package/Edit/Effects/Codex Rise Fade Image.setting`
- `package/Fusion/Macros/Codex/Codex Arc Card.setting`
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
- `Codex Rise Fade Pro Alt`
- `Codex Mask Reveal Pro`

또한 `Effects`에는 아래 이미지용 프리셋이 나타납니다.

- `Codex 3D Arc Image`
- `Codex Rise Fade Image`

Fusion 페이지의 `Macro`에는 아래 카드 모션 매크로를 넣을 수 있습니다.

- `Codex Arc Card`

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
- Direction
- Whole Text Mode
- Travel Distance
- Outro Fade Length
- Character Stagger
- Motion Blur
- Quality
- Shutter Angle
- Intro Blur
- Outro Blur
- Posterize Frames

### Codex Rise Fade Pro Alt

`Codex Rise Fade Pro`의 실험 버전입니다.

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
- Overshoot Strength
- Blur
- Posterize Frames

### Codex Mask Reveal Pro

마스크가 닦이듯 지나가면서 블러와 슬라이드가 같이 걸리는 타이포 버전입니다.

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
- Direction
- Travel Distance
- Intro Blur
- Reveal Softness
- Outro Blur
- Outro Fade Length
- Character Stagger
- Whole Text Mode
- Motion Blur
- Quality
- Shutter Angle

### Codex Rise Fade Image

이미지나 영상 클립에 직접 적용하는 버전입니다.

- Position
- Scale
- Animation Speed
- Ease In
- Ease Out
- X Offset
- Y Offset
- Fade Strength
- Overshoot Strength
- Blur
- Posterize Frames

### Codex 3D Arc Image

2D 이미지/영상 클립을 3D 카드처럼 살짝 회전시키며 arc로 훑는 버전입니다.

- Animation Speed
- Ease In
- Ease Out
- Arc Amount
- Yaw Amount
- Camera Distance
- Height Offset
- Fade Strength
- Tilt X
- Tilt Y
- Tilt Z

### Codex Arc Card

Fusion Composition 안에서 입력 소스에 연결해 쓰는 카드 arc 매크로입니다.

- Input
- Animation Speed
- Ease In
- Ease Out
- Arc Amount
- Yaw Amount
- Camera Distance
- Height Offset
- Fade Strength
- Tilt X
- Tilt Y
- Tilt Z

## 참고

- 기본 `Codex Rise Fade`는 48프레임 기준의 고정형입니다.
- `Codex Rise Fade Pro`는 속도, 방향, 진입량, 아웃 길이를 직접 조절하는 버전입니다.
- `Codex Mask Reveal Pro`는 마스크 리빌과 슬라이드 블러를 같이 쓰는 버전입니다.
- `Codex Rise Fade Image`는 Edit 페이지의 `Effects`에서 이미지/영상 클립에 드래그해서 쓰는 버전입니다.
- `Posterize Frames`를 `1`보다 높이면 일부 프레임을 홀드해서 `Posterize Time`처럼 끊기는 움직임을 만들 수 있습니다.
- `Intro Blur`는 시작할 때 흐렸다가 선명해지는 양입니다.
- `Outro Blur`는 끝부분에서 다시 흐려지는 양입니다.
- `Direction`은 `Up / Down / Left / Right` 진입 방향을 고릅니다.
- `Whole Text Mode`를 켜면 글자별 지연 없이 텍스트 전체가 한 번에 들어옵니다.
- 글자별 순차 진입을 원하면 `Whole Text Mode`를 끄고 `Character Stagger`를 올리면 됩니다.
