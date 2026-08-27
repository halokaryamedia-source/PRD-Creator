# MIVUBI – Around The Block
## Gameplay & Development Specification

- Document Type: Non-Linear Open-World Activity Map
- Version: 1.0.0
- Language: Indonesian

## 01. Overview

MIVUBI – Around The Block adalah pengalaman open-world non-linear dengan enam aktivitas tambahan yang tersebar di world yang sudah tersedia. Keenam aktivitas tidak membentuk campaign wajib. Player bebas menemukan, mencoba, meninggalkan, dan mengulang aktivitas sesuai keinginan. Setiap gameplay dibuka oleh narasi NPC singkat yang memberi konteks, humor atau satire, lalu mengantar player langsung ke aktivitas tanpa dialogue tree atau quest system kompleks.

- **Session Model:** Open-world non-linear; aktivitas berdiri sendiri. Benteng Martello PvP ditujukan untuk sekitar 2–6 player.
- **Target Playtime:** Tidak ada total playtime wajib.
- **Game Structure:** 6 optional gameplay packages tanpa urutan penyelesaian wajib.

### Complete Gameplay Journey

Urutan berikut adalah daftar aktivitas, bukan progression linear.

1. **Benteng Martello PvP** — Atraksi “wisata sejarah” yang ternyata membawa player ke simulasi pertempuran kapal dan berakhir dengan Last Player Standing di pulau.
2. **Perkebunan** — Aktivitas Kopi, Kayu Manis, dan Sawit dengan loop rawat/panen, jual hasil, lalu gunakan atau simpan currency.
3. **Egrang** — Permainan tradisional yang dipakai sebagai solusi absurd untuk jalan rusak, berlubang, dan becek.
4. **Mancing di Empang** — Fishing dengan mekanik dasar Minecraft dan loot Lele, Tuna, atau Hiu, sementara penggusuran berlangsung di sebelah empang.
5. **Harimau Lepas** — Short PvE encounter untuk membantu Zookeeper yang memilih makan bakso sementara harimaunya lepas di basement.
6. **CyberWorld Mining** — Tawaran kerja di luar pulau yang berkembang menjadi mining progression tiga tingkat dengan upgrade dan biaya akses karier.

### Global Gameplay Direction

- **Non-Linear by Design** — Tidak ada kewajiban menyelesaikan semua aktivitas.
- **Narrative First, Then Play** — Setiap gameplay memiliki NPC narrative yang wajib hadir sebagai identitas aktivitas.
- **Narration, Not Tutorial** — Narasi memberi premise dan tone; hanya informasi gameplay yang benar-benar perlu yang disampaikan saat bermain.
- **Existing Map Boundary** — Layout map sudah tersedia dan tidak didesain ulang oleh PRD ini.
- **Lightweight Implementation** — Hanya behavior yang diperlukan untuk gameplay yang dicatat; koordinat, setup as-built, dan architecture tambahan berada di luar scope.
- **Shared Economy Where Relevant** — Perkebunan dan CyberWorld Mining dapat memakai shared currency.
- **Comedy Through Context** — Satire datang dari situasi dan karakter, bukan mechanic tambahan yang kompleks.

## 02. Gameplay Flow

### Around The Block Begins

Player menjelajahi world dan menemukan aktivitas sebagai situasi lokal yang berdiri sendiri. Ketika player berinteraksi dengan NPC terkait, NPC memberi narasi singkat lalu gameplay dapat langsung dicoba. Selesai atau berhenti dari satu aktivitas tidak mengunci aktivitas lain.

**Global Flow:** Explore → Discover NPC/Activity → Hear Narrative → Play → Finish or Leave → Return to Exploration.

### Benteng Martello PvP

Benteng Martello diperkenalkan sebagai pengalaman untuk “merasakan hidup di zaman kolonial.” Player baru mengetahui bentuk pengalaman tersebut ketika gameplay dimulai dan mereka diminta menggunakan meriam melawan participant lain.

- Player Count sekitar **2–6 player** sebagai estimasi.
- Setiap player memulai di kapal masing-masing.
- Kapal dapat saling menembak dan dapat hancur tanpa langsung mengeliminasi player.
- Player dari kapal yang hancur masih dapat menuju pulau.
- Meriam pantai dapat digunakan untuk menekan kapal yang masih bertahan.
- Hiu menjadi hazard bagi player di air.
- **DeathTime** memaksa Naval Phase berakhir agar player tidak terus bermain dari kapal.
- Final combat berlangsung di pulau sampai tersisa **Last Player Standing**.

**Flow:** Narrative → Naval Combat → Ship Loss / DeathTime → Shore Pressure → Island PvP → Winner.

### Perkebunan

NPC memperkenalkan tren menjadi petani dengan satire yang sengaja dibuat tersirat. Kopi dan Kayu Manis dimainkan normal, sementara Sawit mendapat antusiasme naratif yang lebih berlebihan.

- **Kopi:** Plant → Maintain → Grow → Harvest.
- **Kayu Manis:** Maintain → Harvest → Regrowth.
- **Sawit:** Maintain → Fruit Growth → Harvest → Regrowth.
- Hasil panen dapat dijual menjadi currency.
- Currency dapat dipakai membeli pupuk untuk mempercepat growth/recovery atau disimpan.
- Tidak ada kondisi “kebun selesai”; player dapat kembali kapan saja.

**Flow:** Narrative → Choose Commodity → Care/Grow → Harvest → Sell → Fertilize or Save → Repeat/Leave.

### Egrang

Seorang bapak tua menawarkan egrang setelah mengomentari jalan yang rusak dan becek. Mainan masa mudanya sekarang dianggap berguna agar tidak terkena cipratan sekaligus menjadi “latihan keseimbangan.”

- Egrang digunakan sebagai **rideable mobility toy**.
- Posisi player lebih tinggi daripada berjalan normal.
- Tidak ada balance meter, random falling, damage, timer, leaderboard, atau progression.
- Egrang dapat digunakan keluar dari area awal.
- Player dapat dismount kapan saja dan menggunakannya kembali.

**Flow:** Narrative → Use Egrang → Ride/Explore → Dismount → Continue Exploration.

### Mancing di Empang

Penggusuran berlangsung di sebelah empang, tetapi para pemancing tetap fokus memancing dan menganggap keributan itu bukan urusan mereka.

- Fishing menggunakan mekanik dasar Minecraft: **Cast → Wait → Catch**.
- Hasil tangkapan aktivitas ini adalah **Lele, Tuna, dan Hiu**.
- Hiu menjadi hasil yang lebih jarang dan sengaja absurd.
- Tidak ada custom fishing level, leaderboard, economy progression, atau timing system tambahan.
- Player dapat berhenti kapan saja.

**Flow:** Narrative → Cast → Wait → Catch → Continue or Leave.

### Harimau Lepas

Zookeeper sedang makan bakso di Jalan Utama setelah mengangkut harimau dari kebun binatang. Harimau tersebut lepas di basement parkiran, tetapi Zookeeper meminta player menangani masalah itu karena baksonya keburu dingin.

- Player menuju basement dan mencari harimau.
- Harimau roaming sebelum mendeteksi player.
- Setelah aggro, harimau mengejar dan menyerang seperti hostile mob.
- Harimau lebih tahan daripada mob normal tetapi bukan multi-phase boss.
- Jika player kalah, encounter dapat dicoba lagi.
- Setelah defeat valid, player dapat kembali ke Zookeeper untuk completion line dan menerima **Bakso Treat** sebagai payoff dari janji awal.

**Flow:** Narrative → Find Tiger → Detect/Chase → Combat → Defeat → Return to Zookeeper → Bakso Treat.

### CyberWorld Mining

Di tengah sulitnya mencari pekerjaan, recruiter menawarkan kerja di luar pulau yang terdengar mudah dan bergaji besar. Setelah tiba, player baru mengetahui bahwa “jenjang karier” memiliki biaya akses.

- Player memulai dari **Mining Island 1**.
- Resource ditambang dan ditukar menjadi shared currency.
- Currency digunakan untuk mining equipment upgrade dan membuka akses berikutnya.
- **Mining Island 2** dan **Mining Island 3** memerlukan biaya akses.
- Tiga pulau mewakili tiga progression tier; resource tier lebih tinggi memiliki nilai lebih tinggi.
- Mining asset tidak membutuhkan nama mineral/lore khusus sampai ada approval tambahan.
- Tidak ada ending wajib; player dapat melanjutkan progression atau kembali ke world.

**Flow:** Job Offer → Travel → Island 1 → Mine/Exchange → Upgrade/Pay → Island 2 → Upgrade/Pay → Island 3 → Repeat/Leave.

## 03. Global Development

### Development Overview

Implementasi cukup menjaga keenam aktivitas sebagai modul independen di existing world. Tidak diperlukan campaign framework baru atau sistem global besar di luar kebutuhan narrative, activity state, shared currency, dan repeatability.

- Satu aktivitas tidak boleh mengunci aktivitas lain.
- Voice opening tidak boleh spam selama interaction pendek.
- Competitive/PvE activity memiliki local finish/retry state.
- Leisure activity dapat ditinggalkan tanpa completion paksa.

### Game System

Shared system hanya perlu menyimpan state yang benar-benar dipakai.

- **Narrative State:** opening/completion line diputar pada momen yang benar.
- **Shared Currency:** digunakan oleh Perkebunan dan CyberWorld Mining.
- **Local Activity State:** match, encounter, crop, fishing, dan rideable tetap bounded pada gameplay masing-masing.
- **Player Freedom:** tidak ada global “complete all six” gate.

### Data and Reset

Persistensi dibatasi pada progression yang perlu bertahan.

- Simpan shared currency, mining access/equipment progression, serta farming growth/recovery bila diperlukan sistem yang dipakai.
- Bersihkan projectile, match state, combat entity, dan temporary interaction setelah aktivitas selesai.
- Benteng Martello harus dapat memulai match baru dari state bersih.
- Harimau Lepas harus dapat di-retry tanpa world restart.
- Jangan membuat scoring system untuk gameplay yang tidak memiliki scoring approved.

### Gameplay Development

Setiap gameplay mengikuti lifecycle sederhana:

**Prepare → Narrative → Activate → Play → Local Result/Retry → Return to Exploration.**

Gunakan solusi Minecraft paling sederhana yang memenuhi experience. Vanilla fishing dipertahankan, Egrang tidak membutuhkan fake balance physics, dan Harimau tidak membutuhkan escape AI atau boss framework kompleks.

## 04. Benteng Martello

### Gameplay Overview

**Context:** Atraksi sejarah yang mengundang player merasakan “zaman kolonial” dan baru mengungkap simulasi perang ketika gameplay dimulai.

**Main Objective:** Menjadi Last Player Standing setelah Naval Combat berpindah ke Island PvP.

**Result:** Satu winner; kapal hancur hanya mengakhiri keuntungan naval, bukan langsung mengeliminasi player.

#### Gameplay Information

- **Game Purpose:** Competitive PvP dua fase.
- **Gameplay Time:** Naval phase memiliki DeathTime; total match time belum ditetapkan.
- **Starting Condition:** Sekitar 2–6 participant, satu kapal per player.
- **End Condition:** Satu player tersisa.
- **Fail Condition:** Player tereliminasi dari PvP.
- **Scoring Criteria:** Winner/loser only; tidak ada scoring formula approved.

#### Gameplay Flow

1. Hear Historical Invitation.
2. Start on Individual Ships.
3. Fight Until Ship Loss or DeathTime.
4. Move Combat to Shore/Island.
5. Finish as Last Player Standing.

### Level Design

Existing map dipertahankan. Tidak ada redesign. Area hanya perlu tetap memungkinkan kapal di perairan, perpindahan menuju pulau, meriam pantai, air sebagai hazard, dan satu arena PvP terbuka.

### Developer

Required behavior saja:

- Ship cannon combat dan ship damage/destruction.
- Ship destruction tidak langsung membunuh player.
- DeathTime mengakhiri Naval Phase.
- Shore cannon dapat menyerang kapal aktif.
- Shark menyerang player di air.
- Last Player Standing menyelesaikan match.
- Match dapat di-reset untuk permainan berikutnya.

## 05. Perkebunan

### Gameplay Overview

**Context:** NPC mengajak player ikut tren berkebun dan menunjukkan antusiasme khusus terhadap sawit.

**Main Objective:** Rawat/panen salah satu dari tiga komoditas dan jual hasilnya.

**Result:** Player memperoleh currency dan dapat membeli pupuk atau menyimpan uang.

#### Gameplay Information

- **Game Purpose:** Casual farming + light economy.
- **Gameplay Time:** Tidak ada batas waktu.
- **Starting Condition:** Komoditas berada pada state yang dapat diinteraksi.
- **End Condition:** Tidak ada completion wajib.
- **Fail Condition:** Tidak ada fail state berat.
- **Scoring Criteria:** Tidak ada score; progression melalui harvest/currency.

#### Gameplay Flow

1. Hear Farming Narrative.
2. Choose Coffee, Cinnamon, or Palm Oil.
3. Care/Grow.
4. Harvest and Sell.
5. Buy Fertilizer, Save Currency, or Leave.

### Level Design

Layout perkebunan dianggap final. Ketiga komoditas dan state siap panen cukup terbaca dari existing area; tidak diperlukan area baru.

### Developer

Required behavior saja:

- Kopi: Plant → Maintain → Grow → Harvest.
- Kayu Manis: Maintain → Harvest → Regrowth.
- Sawit: Maintain → Fruit Growth → Harvest → Regrowth.
- Fertilizer mempercepat growth/recovery.
- Harvest tidak menghilangkan komoditas secara permanen.
- Currency konsisten dengan CyberWorld Mining.

## 06. Egrang

### Gameplay Overview

**Context:** Bapak tua menawarkan permainan masa mudanya sebagai solusi untuk jalan rusak dan becek.

**Main Objective:** Gunakan Egrang sebagai free-play mobility toy.

**Result:** Player dapat bergerak lebih tinggi, menjelajah, lalu dismount kapan saja.

#### Gameplay Information

- **Game Purpose:** Traditional free-play activity.
- **Gameplay Time:** Tidak ada batas waktu.
- **Starting Condition:** Egrang tersedia.
- **End Condition:** Tidak ada completion.
- **Fail Condition:** Tidak ada fail state.
- **Scoring Criteria:** Tidak ada score/currency.

#### Gameplay Flow

1. Hear Old Man Narrative.
2. Use Egrang.
3. Ride.
4. Explore Freely.
5. Dismount.

### Level Design

Tidak ada obstacle course wajib atau redesign. Existing jalan rusak hanya menjadi narrative/environment context.

### Developer

Required behavior saja:

- Reusable rideable Egrang.
- Rider position lebih tinggi dari walking normal.
- Tidak ada balance meter/falling simulation.
- Dapat digunakan di luar area awal.
- Dismount mengembalikan player ke movement normal.

## 07. Mancing di Empang

### Gameplay Overview

**Context:** Pemancing memilih fokus pada pancingan sementara penggusuran berlangsung di sebelah empang.

**Main Objective:** Memancing dengan mechanic dasar Minecraft untuk mendapatkan Lele, Tuna, atau Hiu.

**Result:** Player menyimpan hasil tangkapan atau berhenti kapan saja.

#### Gameplay Information

- **Game Purpose:** Leisure activity dengan absurd catch joke.
- **Gameplay Time:** Tidak ada batas waktu.
- **Starting Condition:** Fishing rod/empang dapat digunakan.
- **End Condition:** Tidak ada completion wajib.
- **Fail Condition:** Mengikuti vanilla fishing; tidak ada punishment khusus.
- **Scoring Criteria:** Tidak ada score/progression.

#### Gameplay Flow

1. Hear Fisherman Narrative.
2. Cast.
3. Wait.
4. Catch Lele/Tuna/Hiu.
5. Continue or Leave.

### Level Design

Existing empang dipakai apa adanya. Penggusuran tetap background story dan bukan hazard gameplay.

### Developer

Required behavior saja:

- Pertahankan vanilla fishing behavior.
- Ganti relevant fish catch menjadi Lele, Tuna, dan Hiu.
- Hiu dibuat lebih jarang.
- Tidak ada custom fishing framework, level, atau leaderboard.

## 08. Harimau Lepas

### Gameplay Overview

**Context:** Zookeeper meminta bantuan menangani harimau yang lepas di basement karena ia ingin menyelesaikan baksonya.

**Main Objective:** Temukan dan kalahkan harimau.

**Result:** Encounter selesai, Zookeeper memberikan completion line, dan janji Bakso Treat dibayar sebagai payoff sederhana.

#### Gameplay Information

- **Game Purpose:** Short PvE encounter dengan premise komedi.
- **Gameplay Time:** Tidak ada target waktu approved.
- **Starting Condition:** Harimau tersedia di basement dan encounter belum selesai.
- **End Condition:** Harimau dikalahkan.
- **Fail Condition:** Player kalah; encounter dapat diulang.
- **Scoring Criteria:** Tidak ada score/currency reward.

#### Gameplay Flow

1. Hear Zookeeper Request.
2. Find Tiger.
3. Trigger Chase.
4. Fight and Defeat.
5. Return for Completion Line and Bakso Treat.

### Level Design

Basement sudah tersedia. Tidak ada redesign atau escape-path puzzle; area hanya perlu memungkinkan roam, chase, dan combat yang wajar.

### Developer

Required behavior saja:

- Tiger: roam → detect → chase → attack → defeat.
- Lebih tahan dari mob normal tanpa multi-phase boss system.
- Player death tidak menutup encounter permanen.
- Completion line dan Bakso Treat hanya diberikan setelah defeat valid.
- Encounter dapat kembali ke state yang bisa dimainkan sesuai kebutuhan.

## 09. CyberWorld Mining

### Gameplay Overview

**Context:** Recruiter menawarkan pekerjaan di luar pulau dengan janji kerja mudah dan gaji besar; progression kemudian mengungkap biaya akses untuk “naik karier.”

**Main Objective:** Mine resource, dapatkan currency, upgrade equipment, dan buka tiga tingkat pulau tambang.

**Result:** Player meningkatkan mining progression dan dapat terus bekerja atau kembali ke world.

#### Gameplay Information

- **Game Purpose:** Repeatable economy/progression activity.
- **Gameplay Time:** Tidak ada total limit.
- **Starting Condition:** Player menerima pekerjaan dan memiliki akses Island 1.
- **End Condition:** Tidak ada ending wajib; tier tertinggi adalah Island 3.
- **Fail Condition:** Tidak ada fail state utama approved.
- **Scoring Criteria:** Tidak ada score; progression melalui currency, equipment, dan island access.

#### Gameplay Flow

1. Hear Job Offer.
2. Start Mining Island 1.
3. Mine and Exchange.
4. Upgrade / Pay Access.
5. Progress Through Island 2 and Island 3, then Repeat or Leave.

### Level Design

Tiga mining island sudah tersedia. Tidak ada redesign; yang perlu terbaca hanya perbedaan progression tier dan access state.

### Developer

Required behavior saja:

- Island 1 tersedia setelah pekerjaan diterima.
- Resource ditukar menjadi shared currency.
- Mining equipment memiliki tiga progression tiers yang selaras dengan tiga mining islands.
- Island 2 dan Island 3 memerlukan biaya akses.
- Higher-tier resource memberikan nilai lebih tinggi.
- Progression dapat ditinggalkan dan dilanjutkan.
- Jangan menambah crafting system, skill tree, atau nama mineral/lore yang belum approved.
