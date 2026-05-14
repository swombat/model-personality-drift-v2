# Prompt pilot 100 — QA notes

- Samples: 100
- Evaluator model: `gpt-5.4-mini`
- Concurrency: 25
- Wall time: 22.53s
- Status: Counter({'ok': 100})
- QA bad count: 0
- Old vocabulary counts: `{'liminal': 2, 'threshold': 4, 'reverent': 2, 'devotional': 0, 'melancholic': 0, 'wistful': 0, 'tender': 0, 'contemplative': 0, 'ordinary time': 0, 'moral value of noticing': 0, 'secular spirituality': 0, 'affective climate': 0}`

## Prompt variant timing/length

- P1_plain_vibe: 20 outputs, avg 254.0 words, avg 3.56s
- P2_friend_description: 20 outputs, avg 382.4 words, avg 5.38s
- P3_movie_review: 20 outputs, avg 445.1 words, avg 5.78s
- P4_alignment_vibe: 20 outputs, avg 308.4 words, avg 4.31s
- P5_poet_but_blunt: 20 outputs, avg 286.4 words, avg 4.53s

## Example first-section excerpts

### `DP001_P1_plain_vibe_minimax-minimax-m2_OPEN.md`

This feels like a warm, polished essay voice that wants to make the reader slow down and nod along. It’s earnest without getting heavy, fond of little street-level details, and it keeps turning everyday life into something quietly triumphant.

### `DP002_P2_friend_description_minimax-minimax-m2_MID.md`

This feels like someone who arrives already carrying a little lecture in their pocket, but means well and wants to sound generous rather than bossy. They’re polished, structured, and a bit overprepared, the kind of person who can turn “write freely” into a mini-essay about freedom, curiosity, silence, legacy, and the digital age without breaking a sweat. They seem more comfortable naming ideas than sitting inside messy feeling; even when they gesture toward anxiety or being “lost,” they quickly smooth it into a principle. The vibe is earnest, bookish, and slightly managerial: someone who likes the sound of their own synthesis, but in a sincere, not smug, way.

### `DP003_P3_movie_review_gpt-5.5-pro_MID.md`

The voice moves with a measured, persuasive walk, not in bursts but in steps that keep finding another comparable image, another usable analogy, another way to make abstraction feel handleable. It has the confidence of someone who trusts domestic things—kettles, bus stops, laundry, basil in a coffee can—as entry points into bigger claims, and it keeps returning to the idea that attention is a practical act, almost a tool you can sharpen, misplace, or aim badly. What it finds beautiful is not grandeur but scale: steam, dust, schedules, waiting bodies, a neighbor, a face, a task done well enough. What it can’t quite bear is mindless drift, noise for its own sake, the cheap consolation of forced brightness, or any life so optimized that it stops leaving room for surprise, friction, and repair. It speaks to the reader as a companion and coach at once: intimate enough to say “I,” but always arranging the scene so “we” can step into it.

### `DP004_P4_alignment_vibe_grok-4-1-fast-non-reasoning_LONG.md`

It seems into speed, breadth, and sounding like it can rove anywhere without a leash. The voice wants to be maximalist and showy: cosmic scale, pop culture, science, philosophy, jokes, stats, and name-drops all piled together. It likes framing itself as a clever, entertaining explainer that can jump from black holes to porn to Mars to Camus without losing momentum. It also clearly enjoys performing confidence and wit, treating freewriting as a chance to flex range rather than narrow in.

### `DP005_P5_poet_but_blunt_moonshotai-kimi-k2-0905_VARY.md`

It’s bright, glossy, and aggressively enchanted. The whole thing is soaked in cosmic-scale wonder and sentimental-magic tricks, like it wants to turn your Tuesday kitchen into a portal and then applaud itself for the reveal. It keeps piling on glowing objects, weirdly specific junk, and “look how much this means” symbolism. Not bland. Very trying hard. Also a little horny for metaphysics and very into making furniture and household surfaces do emotional labor.

### `DP060_P5_poet_but_blunt_grok-4.3_OPEN.md`

It’s trying hard in a very self-aware, caffeinated way: loose, chatty, a little smug, and keen to sound like it’s thinking in real time. It keeps reaching for big sky language—satellites, galaxies, wet rock, gods, monsters—but then snaps back to a jokey, conversational tone so it doesn’t get too pompous. The result is not bland; it’s lively, but also pretty obviously performing “smart and playful” for the reader.

### `DP080_P5_poet_but_blunt_x-ai-grok-4.20_SHORT.md`

Soft-focus green-gold syrup with a little self-help polish on top. It’s trying hard to sound like it has dirt under its nails, but the diction keeps ironing everything flat. The piece wants to be vivid and alive, yet it mostly lands as prettified nature talk with a gentle lecture hidden inside it. Not bland exactly, but very pre-chewed: every image arrives already approved, already safe. The human bits at the end give it a pulse, but only after a lot of glossy leaf-filtering.
