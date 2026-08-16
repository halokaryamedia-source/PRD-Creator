# Production Asset Requirements

## Global / Shared Assets

### Gameplay Flow 01 — Shared Characters

### 3D Models

#### Custodian Vex
Flow: 01 — Shared Characters
Moment: Used Across the Map
Type: MODEL
Function: Guide NPC used for story, warnings, and completion dialogue.
Visual Brief: Clockwork custodian NPC. Needs the idle, speaking, pointing, alert, and completion animations used by the story.

#### Gremlin
Flow: 01 — Shared Characters
Moment: Used Across the Map
Type: MODEL
Function: Sabotage character used in the final Gallery crossing and the Workshop.
Visual Brief: Small clockwork gremlin NPC. Needs movement, sabotage, taunt, and defeated reactions used in the map.

## The Antechamber

### Gameplay Flow 01 — Arrival & Briefing
### Gameplay Flow 02 — Take Key & Open Seal

### 3D Models

#### Custodian Key
Flow: 01 — Arrival & Briefing
Moment: Entering the Antechamber
Type: ITEM
Function: Opening key used to unlock the first seal.
Visual Brief: Clockwork Vault key for the opening pedestal and pickup, with readable available, picked-up, and accepted states. It must not resemble the end reward.

### UI & Information

#### Custodian Key Prompt
Flow: 02 — Take Key & Open Seal
Moment: Opening the First Seal
Type: UI / TEXT
Function: Tells the player to take the Custodian Key and use it to begin opening the vault.
Content:
```text
TAKE THE CUSTODIAN KEY
The first seal is waiting.
```

## The Resonance Engine

### Gameplay Flow 01 — The Door Remembers
### Gameplay Flow 02 — Search the Chamber
### Gameplay Flow 03 — Tune the Pillars
### Gameplay Flow 04 — Engine Restored

### UI & Information

#### Resonance Engine Entrance Message
Flow: 01 — The Door Remembers
Moment: Entering the Resonance Engine
Type: UI / TEXT
Function: Tells the player the missing clues are somewhere in the chamber without giving the solution.
Content:
```text
RESTORE THE THREE PILLARS

The door remembers only part of the answer.

Everything else you need is somewhere in this chamber.
Look carefully, then bring the Engine back to life.
```

#### Partial Door Target Display
Flow: 01 — The Door Remembers
Moment: Throughout the Resonance Engine
Type: UI / TEXT
Function: Shows Middle = Brown. Left, Right, and Pulse remain unknown.
Content:
```text
LEFT      MIDDLE      RIGHT
 ?         BROWN        ?

PULSE: ?
```

#### Scattered Clue Book Set
Flow: 02 — Search the Chamber
Moment: Searching the Chamber
Type: UI / TEXT
Function: Provides 12 books: 2 rule notes, 8 useful clues, and 2 decoys.
Content:
```text
BOOK 1 — LEVER NOTES
Each pillar is tuned by two levers. Try the upper one, then the lower, and watch how the lamp answers. Different positions reveal different colors.

BOOK 2 — PULSE NOTES
The floor plate never changes a lamp's color. It only changes its rhythm. Step on it and the light will pulse; leave it clear and the light stays steady.

BOOK 3 — LAMP NOTE
The left lamp should have a warm glow. It should not look pale or too dark.

BOOK 4 — OLD ENGINEER'S NOTE
The left light was described as closer to firelight than to the soft color of a flower.

BOOK 5 — MAINTENANCE RECORD
When the Engine was working properly, the left side gave off a gentle glow like warm embers.

BOOK 6 — LAMP RECORD
The right lamp should not use the bright shade of sunlight or the color of fresh leaves.

BOOK 7 — SAFETY NOTE
The correct right-side light is deeper and calmer than the color normally used for danger warnings.

BOOK 8 — OLD VAULT RECORD
The right lamp was once compared to a dark ceremonial cloth used for important occasions.

BOOK 9 — RHYTHM NOTE
When the Engine was balanced, only one lamp pulsed. The middle lamp remained steady.

BOOK 10 — CALIBRATION NOTE
The right lamp remained steady as well. That leaves only one place for the pulse.

BOOK 11 — REPAIR LOG
The lower gear housing was repaired after the last restoration cycle. No further damage was found during inspection.

BOOK 12 — WORKSHOP NOTE
Spare tools were moved to the eastern storage cabinet after the last maintenance shift.
```

#### Resonance Engine Restored Message
Flow: 04 — Engine Restored
Moment: Resonance Engine Restored
Type: UI / TEXT
Function: Confirms the Resonance Engine is restored and points the player to the Broken Gallery.
Content:
```text
ENGINE RESTORED

The pillars are in tune again.
The Broken Gallery is open.
```

## The Broken Gallery

### Gameplay Flow 01 — Enter the Gallery
### Gameplay Flow 02 — First Crossing
### Gameplay Flow 03 — Second Crossing
### Gameplay Flow 04 — Gremlin’s Wager
### Gameplay Flow 05 — When a Path Fails
### Gameplay Flow 06 — Gallery Cleared

### 3D Models

#### Repair Gap Markers
Flow: 01 — Enter the Gallery
Moment: Throughout the Broken Gallery
Type: MODEL
Function: Marks the gaps where the player is allowed to place repair blocks.
Visual Brief: Simple environmental marker or prop placed on repairable gaps. It must stand out from normal blocks without using debug text.

### UI & Information

#### Broken Gallery Entrance Message
Flow: 01 — Enter the Gallery
Moment: Entering the Broken Gallery
Type: UI / TEXT
Function: Tells the player to use the old supplies and repair only marked gaps.
Content:
```text
THE BROKEN GALLERY

The old stores still hold what you need.
Repair only the marked breaks and find a way across.
```

#### First Crossing Message
Flow: 02 — First Crossing
Moment: First Crossing
Type: UI / TEXT
Function: Tells the player more than one route can work without revealing which ones.
Content:
```text
FIRST CROSSING

More than one path can still hold.
Choose carefully before you spend your supplies.
```

#### Second Crossing Message
Flow: 03 — Second Crossing
Moment: Second Crossing
Type: UI / TEXT
Function: Tells the player only one route can work without naming it.
Content:
```text
SECOND CROSSING

Only one path still holds.
Count what you have before you commit.
```

#### Gremlin's Wager Message
Flow: 04 — Gremlin’s Wager
Moment: Gremlin's Final Crossing
Type: UI / TEXT
Function: Explains the final crossing: choose a path and reach halfway before time runs out.
Content:
```text
GREMLIN'S WAGER

Pick a path.
Reach halfway before the clock runs out,
or Gremlin will take that route away.
```

#### Crossing Failure Messages
Flow: 05 — When a Path Fails
Moment: Crossing Failed / Route Lost
Type: UI / TEXT
Function: Shows a short message when a crossing fails or Gremlin removes a route.
Content:
```text
TRY ANOTHER WAY
The crossing has given out.
Take another look at the routes.

PATH LOST
Gremlin took that route.
Find another way across.
```

#### Gallery Cleared Message
Flow: 06 — Gallery Cleared
Moment: Broken Gallery Cleared
Type: UI / TEXT
Function: Confirms the Broken Gallery is cleared and points the player to the Warden Halls.
Content:
```text
GALLERY CLEARED

The last crossing is behind you.
The Warden Halls are ahead.
```

### Audio

#### Gallery Challenge Warning Sound
Flow: 04 — Gremlin’s Wager
Moment: Gremlin's Final Crossing
Type: AUDIO
Function: Signals the start of Gremlin's final Gallery crossing.
Audio Brief: Short mechanical warning sound with a mischievous feel, distinct from normal checkpoint or placement cues. No spoken dialogue.

## The Warden Halls

### Gameplay Flow 01 — Enter the Warden Halls
### Gameplay Flow 02 — Echo Pebble
### Gameplay Flow 03 — Warden Hazards
### Gameplay Flow 04 — Enter the Workshop

### 3D Models

#### Echo Pebble
Flow: 01 — Enter the Warden Halls
Moment: Throughout the Warden Halls
Type: ITEM
Function: Thrown at wall sensors and selected hanging stones.
Visual Brief: Small ordinary stone used in hand and as the projectile. Valid sensor or hanging-stone hits need a readable impact response without making the item look magical.

#### Wall Laser Sensor
Flow: 02 — Echo Pebble
Moment: Throughout the Warden Halls
Type: MODEL
Function: Laser trap that blocks the path and can be disabled with the Echo Pebble.
Visual Brief: Wall-mounted mechanical laser emitter with a visible beam, clear active and temporarily disabled looks, and attached activation/deactivation feedback.

#### Laser Blocker Stone
Flow: 02 — Echo Pebble
Moment: Throughout the Warden Halls
Type: MODEL
Function: Hanging stone that drops into a laser beam and blocks it.
Visual Brief: Stone hanging above selected laser paths. It drops into the beam and stays there as the blocker.

#### Swinging Axe Trap
Flow: 01 — Enter the Warden Halls
Moment: Throughout the Warden Halls
Type: MODEL
Function: Ceiling trap that swings across the corridor.
Visual Brief: Large double-sided axe hanging from the ceiling with a readable left-right swing and reset animation. It must not show an Echo Pebble disable state.

#### Floor Trap
Flow: 01 — Enter the Warden Halls
Moment: Throughout the Warden Halls
Type: MODEL
Function: Floor trap that activates when the player steps on it.
Visual Brief: Floor-mounted trap visually distinct from normal floor blocks and wall sensors, with armed, triggered, and reset looks.

### UI & Information

#### Warden Halls Entrance Message
Flow: 01 — Enter the Warden Halls
Moment: Entering the Warden Halls
Type: UI / TEXT
Function: Introduces the Warden Halls and hints that the Echo Pebble works on wall sensors.
Content:
```text
THE WARDEN HALLS

The Wardens are still listening.
Echo Pebbles can disturb the wall sensors.
Loose stones may break a beam.

The floor and the axes will not be fooled.
```

#### Echo Pebble HUD
Flow: 02 — Echo Pebble
Moment: Throughout the Warden Halls
Type: UI / TEXT
Function: Shows whether the Echo Pebble is ready.
Content:
```text
ECHO PEBBLE · READY
ECHO PEBBLE · RECHARGING
```

#### Warden Halls Cleared Message
Flow: 04 — Enter the Workshop
Moment: Warden Halls Cleared
Type: UI / TEXT
Function: Confirms the Warden Halls are cleared and points the player to the Workshop.
Content:
```text
WARDEN HALLS CLEARED

The inner gate is open.
The Workshop is next.
```

## The Gremlin's Workshop

### Gameplay Flow 01 — Wake Ring One
### Gameplay Flow 02 — Wake Ring Two
### Gameplay Flow 03 — Gremlin Changes the Path
### Gameplay Flow 04 — First Rollback
### Gameplay Flow 05 — Second Rollback
### Gameplay Flow 06 — Wake the Great Orrery

### 3D Models

#### Power Generator
Flow: 01 — Wake Ring One
Moment: Throughout Gremlin's Workshop
Type: MODEL
Function: Power source for the Orrery network.
Visual Brief: Central power machine with a clear output side and distinct offline, live, and interrupted looks. Startup/interruption energy and sound feedback belong to this same setup.

#### 90-Degree Rotator Junction
Flow: 01 — Wake Ring One
Moment: Throughout Gremlin's Workshop
Type: MODEL
Function: L-shaped junction the player rotates to redirect power.
Visual Brief: Compact L-shaped junction with two perpendicular connections, four readable 90-degree orientations, powered and unpowered looks, and a rotation animation.

#### Orrery Ring
Flow: 02 — Wake Ring Two
Moment: Throughout Gremlin's Workshop
Type: MODEL
Function: Ring mechanism used for Ring 1, Ring 2, and Ring 3.
Visual Brief: Reusable clockwork ring with inactive and powered looks plus the motion used during final restoration. The three instances remain distinguishable by position or label while sharing one setup.

### UI & Information

#### Workshop Entrance Message
Flow: 01 — Wake Ring One
Moment: Entering Gremlin's Workshop
Type: UI / TEXT
Function: Tells the player to carry power from the Generator through all three rings.
Content:
```text
AWAKEN THE ORRERY

Carry power from the Generator through all three rings.
Keep every earlier ring alive as you move forward.
```

#### Orrery Ring Status
Flow: 02 — Wake Ring Two
Moment: Throughout Gremlin's Workshop
Type: UI / TEXT
Function: Shows one current power state for each Orrery ring: POWERED or NO POWER.
Content:
```text
RING 1 · POWERED
RING 1 · NO POWER

RING 2 · POWERED
RING 2 · NO POWER

RING 3 · POWERED
RING 3 · NO POWER
```

#### Route Swap Message
Flow: 03 — Gremlin Changes the Path
Moment: Gremlin Changes the Route
Type: UI / TEXT
Function: Tells the player the old route is blocked and another route is open.
Content:
```text
GREMLIN'S WORK

Your old path is blocked.
Another way has opened.

Find it and bring Ring Two back to life.
```

#### Ring One Power-Loss Message
Flow: 04 — First Rollback
Moment: Ring One Loses Power
Type: UI / TEXT
Function: Tells the player Ring One lost power after Gremlin's sabotage.
Content:
```text
RING ONE LOST POWER

Gremlin knocked the power line out.
Restore Ring One.
```

#### Ring Two Power-Loss Message
Flow: 05 — Second Rollback
Moment: Ring Two Loses Power
Type: UI / TEXT
Function: Tells the player Ring Two lost power after Gremlin's sabotage.
Content:
```text
RING TWO LOST POWER

Gremlin struck the power line again.
Restore Ring Two.
```

## Vault Restored

### Gameplay Flow 01 — The Vault Awakens
### Gameplay Flow 02 — The Way Home

### 3D Models

#### Clockwork Wayfinder
Flow: 01 — The Vault Awakens
Moment: Vault Restored
Type: ITEM
Function: Reward item shown after the vault is restored.
Visual Brief: Cosmetic reward with a distinct Clockwork Vault silhouette and a clear reward-reveal state. It should not imply new gameplay power.

### UI & Information

#### Vault Restored Message
Flow: 02 — The Way Home
Moment: Way Home
Type: UI / TEXT
Function: Confirms the vault is restored and points the player to the open gateway.
Content:
```text
THE CLOCKWORK VAULT IS RESTORED

The gateway is open.
Follow the light home.
```
