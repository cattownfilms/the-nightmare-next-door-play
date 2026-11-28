# The Nightmare Next Door

[Play the game](https://cattownfilms.github.io/the-nightmare-next-door-play/)

## v0.21.8-o11-18 — completed O11 art and gameplay corrections

Publishes the reviewed native-detail hero and boss art, boss attack indicators and recovery cues, Bex directional equipment/throw corrections, Alien and Hunter action repairs, Clown balloon/string art, and the completed results, rescue, Practice and first-aid fixes. This is the tested 0.21.8-o11-18 candidate, not a repackaging of 0.21.7.

37 of 39 reviewed art rows are resolved, plus three prior Bex corrections. Two native east-facing replacements remain unavailable: Hockey Mask `heavy_chop_chain_east` and Striped Sweater `claw_flurry_east`. Their existing animations remain; this release does not claim those replacements are finished.

Source: `2001c6143b42e0a6c4d2d73d88a174b1b8c7ee7d` (private repository). The public package removes source/review provenance and the development animation-audit interface. Native runtime art, frame timing, registration, and accepted gameplay are retained. No private generator, Level Lab or tileset experiment is included.

Validation: retained isolated-browser gameplay/art acceptance; additional public-package startup, exact selected-asset hashes and deployment checks. Physical-phone acceptance and sustained device performance remain manual.

Rollback: release `v0.21.7-boss-art-1`, public commit `8a341b0fa7f7b1a78bb429b756fe85a94a10a9a3`. Updates use the existing pinned release archive and Pages Actions workflow; generated HTML and source history are not committed here.

### Runtime asset notice

The runtime still includes legacy game-derived environment, actor/item artwork and audio effects alongside the supplied original music and newer character/boss artwork. Their inclusion is not a claim of rights clearance. Required runtime assets have not been silently deleted. Raw recordings, ROM files, private reports, saves and credentials are excluded.

## v0.21.1-boss-art-1

Art-only cleanup of nine boss sheets: detached extra weapons, claws and debris removed from Hockey Mask, Striped Sweater, Ghost Mask, Alien, Hunter, Clown, Flower and Wolf. Intentional weapons, balloons, limbs and effects remain. Gameplay, frame timing, pivots and saves are unchanged. All 23 affected animation sequences and eight Practice renders checked; unresolved fused or clipped source art remains unchanged.

### Preserved O11 corrections

O11 playtest corrections: drippy campaign titles above yellow tagline streaks with thin white lettering outlines; stable player camera during living-exit pursuit; persistent SHOOT THE EXIT DOOR / ENTER THE EXIT guidance; immediate four-sided boss-domain activation and obstacle-aware connected-area pursuit; Hockey Mask shoreline routing and existing water signatures retained. Reveal/portal/results transitions and collected-coin accounting are corrected without changing campaign order or difficulty balance.

Level 1 is **There Goes the Neighborhood**, with **The Nightmare Begins!!!** on the yellow streak. Existing saves and explicit Title Studio edits remain intact. Focused engine checks and Chromium portrait/landscape checks passed; physical-phone acceptance remains manual.

### Preserved campaign

New campaigns activate the twenty approved chapters, their actual biomes and the ten distinct required encounters. Hockey moves to level7; level8 has no required boss. Wolf debuts at5 as a heavy. Cheerleaderpede remains last at20; legitimate victory offers End Run or Continue Endless at21.

| Level | Title | Biome / profile | Required boss |
|---|---|---|---|
| 01 | There Goes the Neighborhood | neighborhood / neighborhood | — |
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

This repository hosts the pinned public runtime and verified Pages workflow. `release.json` pins exact source, archive and index hashes. Rollback: `v0.21.1-o11-1`, public `c9f33aa945fb94b63433ed56e094728d06eec08f`. Source development remains private.
