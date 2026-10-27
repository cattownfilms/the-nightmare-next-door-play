# The Nightmare Next Door — public gameplay deployment

Only hosting configuration and release receipts live in this repository. The development source and its history remain private in cattownfilms/the-nightmare-next-door. Runtime JavaScript, playable sprites and audio are intentionally public in the release package and Pages artifact.

This build retains legacy Zombies Ate My Neighbors-derived terrain, campaign/NPC/enemy/item imagery and sound effects alongside newer character artwork and the user's original soundtrack. No rights clearance is asserted. No ROM files, raw source videos, saves, credentials, extraction reports or private audit catalogs are distributed.

The public build externalizes byte-identical PNG/WAV resources and unchanged compressed MP3 audio (ID3 provenance tags removed only from public copies), strips private provenance, uses opaque runtime origin identifiers where legacy renderer comparisons require them, and fetches external soundtrack files. Gameplay and the local build are unchanged. The developer-only animation audit loader is excluded.

## Update procedure

1. Verify the intended private source commit and its existing production build receipt; preserve localhost and saves.
2. Prepare a separate audited public package; never copy the checkout or its dist audit directories wholesale. Validate mobile startup and all referenced resources. Record original build hash and sanitized public index hash.
3. Upload `site.tar.gz` as a new uniquely tagged public release (do not replace an older release). Update `release.json` with the exact URL, archive SHA-256 and source commit. Commit only hosting configuration/receipts.
4. Dispatch `Publish verified gameplay`. It validates the archive paths, size, contents and every file hash, uploads a Pages artifact, and deploys with only Pages write/OIDC permissions. No private-repository token is used by Actions.
5. Verify the returned HTTPS page and resources without authentication and run browser startup checks. A successful push alone is not deployment verification.

The public origin has separate browser storage from localhost:8001. Save export/import is optional and manual; publication never clears or migrates local saves automatically. First load downloads substantial artwork; physical-phone acceptance and listening remain manual.
