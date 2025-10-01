# NeverEndingQuest Modules

A collection of downloadable adventure modules for [NeverEndingQuest](https://github.com/MoonlightByte/neverendingquest), an AI-powered tabletop RPG system. Each module is a complete, self-contained adventure with locations, NPCs, quests, and encounters ready to play.

## Features

- **Drop-in Installation** - Just copy to your modules folder
- **Full AI Integration** - Rich narratives and dynamic responses
- **Level-Appropriate Content** - Balanced encounters and progression
- **Themed Adventures** - Seasonal, genre-specific, and classic fantasy

## Available Modules

| Module | Levels | Theme | Est. Hours | Status |
|--------|--------|-------|------------|--------|
| [The Pumpkin Kings Curse](#the-pumpkin-kings-curse) | 1-3 | Halloween Horror | 4-6 | Ready |

---

### The Pumpkin Kings Curse

**Levels:** 1-3
**Theme:** Halloween Horror
**Estimated Playtime:** 4-6 hours
**Locations:** 6 areas, 27 explorable locations

A cursed harvest moon rises over Hollowfen, and the dreaded Pumpkin King awakens. Navigate haunted fields, creeping graveyards, and a living mansion to break the curse before the final midnight bell tolls.

**Features:**
- 7 recruitable NPCs with unique personalities
- Multi-phase boss encounter with environmental hazards
- Fear mechanics and courage boons
- Rich exploration with optional side quests
- Atmospheric Halloween setting

**[Download Module](./The_Pumpkin_Kings_Curse)**

---

## Installation

1. **Download a fresh copy** of [NeverEndingQuest](https://github.com/MoonlightByte/neverendingquest)
2. **Delete any unwanted modules** from the `modules/` folder (the fresh install comes with sample modules)
3. **Download the module(s)** you want from this repository
4. **Copy the module folder(s)** to your `neverendingquest/modules/` directory
5. **Launch the game** - Your chosen modules will auto-detect

**Example:**
```
neverendingquest/
└── modules/
    ├── The_Thornwood_Watch/        <-- Starter module (delete if unwanted)
    ├── Keep_of_Doom/               <-- Starter module (delete if unwanted)
    └── The_Pumpkin_Kings_Curse/    <-- Place downloaded module here
```

---

## Updating Modules

**IMPORTANT:** If you have an existing game in progress, updates will only affect the `*_BU.json` (backup) files. Your live game files (which contain player progress) are safe.

To get updates:
1. Pull the latest changes from this repository
2. Overwrite the module folder in your installation
3. Your game progress is preserved in the live `.json` files

---

## Module Structure

Each module contains:

```
Module_Name/
├── areas/                    # Location files
│   ├── AREA001_BU.json      # Clean source (restored on updates)
│   └── AREA001.json         # Live game file (preserves player progress)
├── media/                    # Images and audio
├── encounters/               # Combat encounters
├── characters/               # NPCs and party data
├── module_plot_BU.json      # Clean plot source
├── module_plot.json         # Live plot (tracks quest progress)
└── module_context.json      # Module metadata
```

**Key Concept:** `*_BU.json` files are clean source files. Regular `.json` files contain your game state and progress.

---

## Contributing

Want to share your own module? Check out [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on:
- Module quality standards
- Submission process
- Schema compliance
- Testing requirements

---

## Requirements

- [NeverEndingQuest](https://github.com/MoonlightByte/neverendingquest) (main game engine)
- Python 3.8+
- OpenAI API key (for AI dungeon master)

---

## License

Each module may have its own license. See individual module folders for details.

**The Pumpkin Kings Curse:** Created by MoonlightByte. Free to use and modify for personal gameplay.

---

## Support

- **Issues:** Report bugs or request features in the [main NeverEndingQuest repository](https://github.com/MoonlightByte/neverendingquest/issues)
- **Discussions:** Join the community discussions for module ideas and support

---

**Happy Adventuring!**
