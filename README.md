# The Nightmare Next Door

[Play the game](https://cattownfilms.github.io/the-nightmare-next-door-play/)

## v0.20.0-boss-cards-1

This release adds the implemented boss foundation/signature mechanics and illustrated level introductions. Combat uses readable tells, committed strikes and recovery windows. Introductions use the approved illustrated backgrounds, glyph lettering, a separate yellow tagline streak, character credit, fresh-input skip and reduced-motion presentation.

Current saved campaigns retain their versioned level order: ten required bosses through the level-20 finale, with endless beginning at 21. Hockey Mask remains at level 8 in the active mapping. The new twenty-chapter title plan is available in Title Studio; it does not silently move bosses or rename incompatible stages in existing runs. Actual gameplay cards use the current level's compatible copy and biome.

| Encounter | Included behavior |
|---|---|
| hockey-mask | Shared-controller water breach/short landing, checked retreat and dry exit, surface ripples/splash, marked-neighbor hunt, ordinary-shot/freeze/body-block interrupt, phase-entry and per-hunt heal caps, invalidation/timeout/save cleanup; intact 0289 v2 body with reused retreat pose. |
| night-manager | Warned short shutter with checked escape perimeter, pursuit and removal on recovery/death/load. |
| lawn-enforcement | Directional delayed sweep lanes and a scoped supported hedge shortcut. |
| ghost-mask | Readable edge approach and false silhouettes, true directional tell, committed rush and punishable recovery. |
| striped-sweater | Pursuit rake and distinct delayed claw-mark lanes. |
| biomechanical-alien | Skitter/tail pressure, collision-checked reposition and vulnerable recovery. |
| armored-hunter | Locatable shimmer, acquisition then locked laser shot, renewable hit/touch disruption, bounded cloak and centrally tuned 20-second visible combat window. |
| balloon-clown | Bounded ascent/casting, reachable anchor or ordinary-hit descent counter, grounded punish and warned return. |
| flower-headed-creature | Closed defense with approach/hit opening counter, petal sectors and exposed bloom; scoped green arena dressing. |
| cheerleaderpede | Committed charge, visible burrow trace/emergence and recovery; no echoes. |
| wolf-creature | Howl/pounce commitment with punishable misses. |
| large-mutant | Bounded momentum charge and supported wall-impact stagger. |
| tricycle-puppet | Readable driving line and stopped knockdown punish, rendered with an existing intact final death-art pose while logically alive. No newly authored dismount/on-foot animation. |
| root-rot | Existing optional gardener miniboss gets seed/root-line pressure and exposed collapse using existing poses; no required-boss promotion. |
| BogBird | Deferred proposed optional apex; no registry entry or unlock invented. |

Existing character cinematics, Level Complete/Game Over artwork, weapons, shops, music and the skittering exit remain. The optional Root Rot stays a miniboss; Wolf, Mutant and Tricycle stay heavies. Tricycle knockdown and water retreat reuse existing art; no newly authored dismount or retreat animation is claimed.

No Phase Three echoes, mastery remixes, BogBird expansion, sharks or chapter-order migration are included. Native and emulated-browser checks do not establish physical-controller compatibility or sustained phone performance.

## Distribution

This repository hosts only the audited public runtime release and its pinned Pages deployment workflow. Source development remains private. `release.json` pins the source commit, archive and index hashes; deployment verifies the archive before publishing. The preceding rollback release is `v0.18-exit-skitter-1` (public commit `39a45be0761ca18ae19aa0edf484896a7c9695a0`).
