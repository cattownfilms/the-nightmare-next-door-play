# The Nightmare Next Door

[Play the game](https://cattownfilms.github.io/the-nightmare-next-door-play/)

## v0.21.0-itinerary-1

New campaigns activate the twenty approved chapters, their actual biomes and the ten distinct required encounters. Hockey moves to level7; level8 has no required boss. Wolf debuts at5 as a heavy. Cheerleaderpede remains last at20; legitimate victory offers End Run or Continue Endless at21.

| Level | Title | Biome / profile | Required boss |
|---|---|---|---|
| 01 | The Nightmare Begins!!! | neighborhood / neighborhood | — |
| 02 | So I Manage an Axe Murderer | mall / retail | night-manager |
| 03 | The Hedges Have Eyes | yards / garden | — |
| 04 | Lawn and Disorder | yards / hedge | lawn-enforcement |
| 05 | Full Moon on Maple St | neighborhood / neighborhood | — |
| 06 | American Scream | neighborhood / courtyard | ghost-mask |
| 07 | Thursday the 12th | yards / lake | hockey-mask |
| 08 | CHOPPING Mall | mall / retail | — |
| 09 | Night Swim, No Lifeguard | yards / pools | — |
| 10 | Bad Neighbor on Elm St | neighborhood / street | striped-sweater |
| 11 | The Food Court of the Damned | mall / food-court | — |
| 12 | Something in the Leftovers | mall / loading | biomechanical-alien |
| 13 | Pet Sematary Sale | yards / burial-yard | — |
| 14 | To Catch a Predator | yards / hunting-ground | armored-hunter |
| 15 | Child's Play, No Refunds | mall / arcade | — |
| 16 | IT FLOATS | mall / atrium | balloon-clown |
| 17 | The Park and the Wicked | neighborhood / park | — |
| 18 | Little Shop of Horrors | mall / overgrown-mall | flower-headed-creature |
| 19 | Lawn of the Dead | yards / garden | — |
| 20 | Three Cheers for the Apocalypse | neighborhood / school | cheerleaderpede |

Boss domains use retail shelving/stockroom lanes, hedge clearings, courtyards, real lake shore, street court, hardware loading bay, hunting ground, mall atrium, planted mall garden center, and the finale school gym. Only the new Cheerleaderpede domain uses gym court terrain. Existing attacks, counters, doorway activation, reveal, compass and living exit remain. Generated layouts keep connected escape lanes and a bounded same-profile fallback.

Main menu: Continue, New Game, Options, Extras. Options directly contains Level Select and Boss Practice. The twenty-stage replay picker unlocks from validated cleared-stage and required-defeat receipts, protects campaign saves/inventory/rewards, and returns safely. Level1 is initially available. Legacy saves without reliable clear receipts do not fabricate unlocks from a high level number. Title Studio remains in Extras; chapter edits and red/green presentation share the gameplay renderer.

Compatibility exception: existing runs retain their old schedule AND deterministic arena generator, including old level8 Hockey and legacy gym domains; no loaded map is rebuilt. New itinerary runs and Boss Practice use the new profiles. Nine-level saves retain their completion contract. Explicit custom cards remain; new-run automatic chapter defaults use the approved manifest. No data clearing or save-origin change.

Level9 has real navigable pools, not the deferred circling/chomping shark enemy. No Phase Three, BogBird expansion, new attacks, raw reference videos, private Level Lab or tileset experiments are included. Physical Android/controller acceptance and sustained phone performance are unmeasured.

## Distribution and rollback

This repository hosts the pinned public runtime and verified Pages workflow. `release.json` pins exact source, archive and index hashes. Rollback: `v0.20.1-menu-cards-1`, public `8ad4a982ae790e680003cff185caaa5538281bca`. Source development remains private.
