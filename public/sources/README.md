# Bascorro robot documentation — reviewed focused pass

Documentation snapshot: 2026-10-29. Start with the robot guides below; shared subsystem cards are linked separately.

**46 source/citation-checked reports: 16 shared cards, 18 robot-specific investigations and 12 guides.**
The 13 flagged drafts were reviewed and rewritten; five earlier failures were recovered. Other checked drafts retain their original source checks.

These are source-based drafts. No build, ROS launch, simulator, robot motion or hardware validation was performed.
Source/path/hash checks do not establish full semantic correctness or safe operation. Read the open questions in each guide.

[Review notes and known issues](REVIEW-NOTES.md) · [Shared cards](Shared/README.md) · [Branch comparison](BRANCH-COMPARISON.md)

## Alphonse
Branch `ALPHONSE_NEW_V2`, commit `adacde8f6e01e6439d170fb6bce025acc051bfa3`.

- [Alphonse guide: Setup and prerequisites](Alphonse/focus-guide-setup.md)
- [Alphonse guide: Architecture and interfaces](Alphonse/focus-guide-architecture.md)
- [Alphonse guide: Operation and troubleshooting](Alphonse/focus-guide-operation.md)
- [Alphonse guide: Robot-specific settings, differences and review gaps](Alphonse/focus-guide-differences.md)

[All Alphonse investigations](Alphonse/README.md)

## Chronus
Branch `CHRONUS_NEW`, commit `54998e7c56e5b2cce4c1c533758c7d2f2cf7698b`.

- [Chronus guide: Setup and prerequisites](Chronus/focus-guide-setup.md)
- [Chronus guide: Architecture and interfaces](Chronus/focus-guide-architecture.md)
- [Chronus guide: Operation and troubleshooting](Chronus/focus-guide-operation.md)
- [Chronus guide: Robot-specific settings, differences and review gaps](Chronus/focus-guide-differences.md)

[All Chronus investigations](Chronus/README.md)

## Orion
Branch `ORION_NEW`, commit `dba5be3fefbada854b8d6c11d6655f479b482574`.

- [Orion guide: Setup and prerequisites](Orion/focus-guide-setup.md)
- [Orion guide: Architecture and interfaces](Orion/focus-guide-architecture.md)
- [Orion guide: Operation and troubleshooting](Orion/focus-guide-operation.md)
- [Orion guide: Robot-specific settings, differences and review gaps](Orion/focus-guide-differences.md)

[All Orion investigations](Orion/README.md)

## Provenance and scope

verification.json records source snapshots, read paths and available reviewer ranges. manifest.json contains SHA-256 hashes for every package file except the manifest itself.
The 897 pending exhaustive-audit jobs remain deferred in the workstation; historical partial audit drafts are outside this focused snapshot.
This ZIP contains documentation and provenance only. Repositories, models, databases, credentials and chat data are outside the package.
