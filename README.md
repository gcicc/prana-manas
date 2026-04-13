# Prana Manas - Meditation & Mindfulness

A progressive web app for meditation, mindfulness, and loving-kindness practice. Part of the **Prana Suite** of wellness apps.

**Live:** https://gcicc.github.io/prana-manas/

## Features

### Meditation Timer
- **Large circular timer display** with visual progress ring
- **Preset durations:** 5, 10, 15, 20, 30, 45, 60 minutes
- **Custom duration** input for any length
- **Ambient sounds:**
  - Silence
  - Soft drone (60Hz sine wave)
  - Rain (filtered white noise)
  - Singing bowl loop (repeats every 30s)
- **Bell notifications:**
  - Start bell: Single singing bowl tone
  - Interval bells: Every 5–10 minutes (optional)
  - End bell: 3 gentle strikes
- **Screen stays on** during meditation (Wake Lock API)
- **Immersive mode** hides UI for full-screen focus

### Guided Prompts (Metta / Loving-Kindness)
- Toggle "Guided" mode to enable prompts during meditation
- 20+ rotating prompts including:
  - "May I be happy. May I be peaceful. May I be free from suffering."
  - "May all beings be happy..."
  - "Breathe in compassion. Breathe out tension."
  - "Notice your thoughts without judgment. Let them pass like clouds."
- Prompts appear every 2–3 minutes with varied timing
- Focus on compassion for self, loved ones, and all beings

### Session Log & Tracking
- **Auto-logging** after each meditation with date, duration, and type
- **Mood rating** (1–5 emoji scale) after session
- **Optional journal note** to capture reflections
- **Stats dashboard:**
  - Total sessions
  - Total minutes meditated
  - Current streak
  - Longest streak
- **Calendar view** showing meditation days across any month
- **History list** of recent 20 sessions with details

### Prana Hub
- Quick links to other Prana Suite apps:
  - Prana Breathing (guided breathwork)
  - Prana Sound (healing tones)
  - Prana Drishti (visual focusing)
  - Prana Sparsha (touch patterns)
  - Sound Palette (custom soundscapes)

## Design System

Follows **Prana theme** design from MobileTapper:
- **Background:** `#0d1117` (dark)
- **Cards:** `#161b22` (darker gray)
- **Accent:** `#c4a882` (warm sand/gold)
- **Fonts:** Cormorant Garamond (display) + Inter (body)
- Spacious, calm layout with ample breathing room
- Responsive design for phone, tablet, desktop

## Technology

- **Vanilla HTML/CSS/JS** — no frameworks, no dependencies
- **Web Audio API** for bells and ambient sounds
- **LocalStorage** for session persistence
- **Wake Lock API** to keep screen on
- **Service Worker** for offline-first caching
- **Progressive Web App** (installable on home screen)

## Installation

### Use as a PWA
1. Visit https://gcicc.github.io/prana-manas/ on iOS or Android
2. Tap "Share" → "Add to Home Screen" (iOS) or "Install" (Android)
3. Icon appears on home screen; works offline after first load

### Local Development
```bash
git clone https://github.com/gcicc/prana-manas.git
cd prana-manas
python -m http.server 8000
# Open http://localhost:8000
```

## File Structure

```
prana-manas/
├── index.html           # Complete single-file app
├── manifest.json        # PWA manifest
├── sw.js               # Service worker (offline support)
├── generate-icons.py   # Icon generation (Pillow)
├── icon-192.png        # App icon (192px)
├── icon-512.png        # App icon (512px)
├── icon-*-maskable.png # Maskable icons for adaptive display
└── README.md           # This file
```

## Privacy

- No tracking, no analytics, no ads
- No accounts, no login required
- All data stored **locally** in browser (LocalStorage)
- Session logs never leave your phone
- Works completely offline after installation

## Browser Support

- Chrome/Edge 40+
- Firefox 42+
- Safari 11.1+ (iOS 11.3+)
- All modern browsers with Web Audio + Service Workers

## Related Apps

Part of the **Prana Suite**:
- [Prana Breathing](https://github.com/gcicc/prana-breathing) — Guided breathwork
- [Prana Sound](https://github.com/gcicc/prana-sound) — Singing bowls & tones
- [Prana Drishti](https://github.com/gcicc/prana-drishti) — Visual meditation
- [Prana Sparsha](https://github.com/gcicc/prana-sparsha) — Touch patterns
- [Sound Palette](https://github.com/gcicc/sound-palette) — Custom soundscapes

## License

Private (Portfolio project)

---

**Built with ❤️ by Greg Cicconetti** — MobileTapper portfolio series
