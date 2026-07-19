# UX Epic - OPEN QUESTIONS: Design Questions

The following layout and interaction issues remain open:

---

## 1. Native Window Frame Override
- **Issue:** Should K.A.O.S hide the standard Windows title bar (Minimize, Maximize, Close buttons) and draw a custom frameless glass header instead?
- **Trade-offs:**
  - **Custom Frame:** Looks premium, matches the glassmorphism aesthetic perfectly.
  - **Native Frame:** Standard behavior, supports Windows snap layouts natively without writing custom Tauri window handlers. (Recommended to keep native snapping to avoid UX bugs).

---

## 2. Voice Input UI integration
- **Issue:** Where should the voice control button reside?
- **Options:**
  - Placed in the command palette.
  - A persistent microphone icon inside the chat prompt input.
  - Activates globally via a hotkey (e.g., `Caps Lock` double-tap).
