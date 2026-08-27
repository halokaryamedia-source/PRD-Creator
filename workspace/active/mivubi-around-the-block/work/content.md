# MIVUBI – Around The Block
## Gameplay & Development Specification

- Document Type: Non-Linear Open-World Activity Map
- Version: 1.0.0
- Language: Indonesian

## 01. Overview

MIVUBI – Around The Block adalah pengalaman open-world non-linear yang menempatkan enam aktivitas tambahan di dalam world yang sudah tersedia. Aktivitas tidak membentuk campaign wajib dan tidak harus diselesaikan seluruhnya. Player bebas menemukan, mencoba, meninggalkan, dan mengulang aktivitas sesuai keinginan. Setiap aktivitas dibuka oleh narasi NPC singkat yang menjelaskan situasi, memberi konteks humor atau satire, lalu mengarahkan player ke gameplay tanpa dialogue tree atau quest system yang kompleks.

- **Session Model:** Open-world non-linear; aktivitas bersifat independen. Benteng Martello PvP ditujukan untuk sekitar 2–6 player.
- **Target Playtime:** Tidak ada total playtime wajib; setiap aktivitas dapat dimainkan secara opsional dan sebagian dapat diulang.
- **Game Structure:** 6 optional gameplay packages tanpa urutan penyelesaian wajib.

### Complete Gameplay Journey

Urutan berikut adalah daftar aktivitas, bukan progression linear.

1. **Benteng Martello PvP** — Player mengikuti “wisata sejarah” yang ternyata membawa mereka ke simulasi pertempuran kapal, lalu menyelesaikan PvP di pulau sampai tersisa satu pemenang.
2. **Perkebunan** — Player mencoba tiga aktivitas perkebunan—kopi, kayu manis, dan sawit—memanen hasil, menjualnya, lalu menggunakan atau menyimpan currency.
3. **Egrang** — Player menggunakan egrang sebagai permainan tradisional sekaligus solusi absurd untuk melewati jalan rusak dan becek tanpa terkena cipratan.
4. **Mancing di Empang** — Player berhenti sejenak untuk memancing dengan mekanik dasar Minecraft sementara penggusuran berlangsung di sebelah empang; hasil pancing diganti menjadi Lele, Tuna, atau Hiu.
5. **Harimau Lepas** — Player membantu Zookeeper yang sedang makan bakso dengan menangani harimau lepas di basement parkiran.
6. **CyberWorld Mining** — Player menerima tawaran kerja di luar pulau, menambang resource, menghasilkan currency, meng-upgrade equipment, dan membayar akses untuk membuka pulau tambang berikutnya.

### Global Gameplay Direction

- **Non-Linear by Design** — Tidak ada kewajiban menyelesaikan keenam aktivitas atau memainkan urutan tertentu.
- **Narrative First, Then Play** — Setiap gameplay memiliki NPC narrative yang memberi premise, tone, dan alasan mencoba aktivitas sebelum gameplay berjalan.
- **Simple NPC Delivery** — NPC berfungsi sebagai narator; tidak diperlukan dialogue tree atau percabangan quest kompleks.
- **Existing Map Boundary** — Layout map dianggap sudah tersedia. Dokumen ini tidak mendesain ulang map dan hanya menyimpan kebutuhan gameplay yang harus terbaca di area yang sudah ada.
- **Lightweight Development Scope** — Developer detail dibatasi pada perilaku yang diperlukan untuk membuat briefing gameplay bekerja; detail as-built, koordinat, dan setup teknis tidak termasuk scope PRD.
- **Shared Economy Where Relevant** — Perkebunan dan CyberWorld Mining dapat menggunakan shared currency. Aktivitas lain tidak diwajibkan memberi reward ekonomi.
- **Comedy Through Context** — Humor dan satire berasal dari situasi serta narasi, sementara gameplay tetap sederhana dan mudah dipahami.

## 02. Gameplay Flow

### Around The Block Begins

Player menjelajahi world tanpa jalur objective utama yang memaksa mereka menyelesaikan seluruh aktivitas. Setiap gameplay ditemukan sebagai situasi lokal yang berdiri sendiri. Ketika player mendekati NPC terkait, NPC menyampaikan narasi singkat, lalu player dapat langsung mencoba aktivitas atau melanjutkan eksplorasi.

- **Discover an Activity** — Player menemukan NPC atau situasi yang menandai aktivitas opsional.
- **Hear the Premise** — NPC menjelaskan konteks dengan tone komedi atau satire.
- **Enter the Gameplay** — Setelah narasi, aktivitas dapat dimainkan tanpa dialog bercabang.
- **Leave Freely** — Aktivitas non-kompetitif dapat ditinggalkan kapan saja; aktivitas match/encounter mengikuti kondisi akhir lokalnya.
- **Return to Exploration** — Selesai atau berhenti dari satu aktivitas tidak mengunci aktivitas lain.

**Transition:** Tidak ada transition global antar-objective. Setiap gameplay mengembalikan player ke kebebasan eksplorasi setelah aktivitas lokal selesai atau ditinggalkan.

### Benteng Martello PvP

Benteng Martello diperkenalkan sebagai pengalaman untuk “merasakan hidup di zaman kolonial.” Player baru menyadari bentuk pengalaman tersebut ketika mereka ditempatkan pada kapal bersenjata dan diminta menembakkan meriam ke lawan.

- **Historical Attraction Setup** — NPC mengajak player mencoba pengalaman sejarah dan menyarankan membawa setidaknya satu player lain.
- **Naval Combat** — Setiap player memulai di kapal masing-masing dan dapat menembaki kapal lawan dengan meriam.
- **Ship Loss Is a Transition** — Kapal yang hancur tidak langsung mengeliminasi player; player tetap dapat menuju pulau untuk melanjutkan PvP.
- **Shore Pressure** — Player yang lebih dulu mencapai pulau dapat menggunakan meriam di pinggir pantai untuk menekan kapal yang masih bertahan.
- **DeathTime** — Naval phase memiliki batas waktu agar match tidak berhenti pada pertempuran kapal tanpa akhir. Kapal yang masih aktif dipaksa keluar dari fase naval.
- **Island Finish** — Seluruh survivor melanjutkan PvP di arena terbuka sampai tersisa satu player.
- **Water Hazard** — Hiu berkeliling di perairan dan menjadi ancaman bagi player yang terlalu lama berada di air.

**Transition:** Last Player Standing dinyatakan sebagai pemenang dan match Benteng Martello selesai.

### Perkebunan

Perkebunan diperkenalkan oleh NPC yang sangat bangga dengan meningkatnya minat orang terhadap profesi petani, termasuk “wajah-wajah gagah berani” dari latar yang tidak disangka. Satire terutama muncul dari antusiasme berlebihan terhadap sawit, sementara kopi dan kayu manis tetap dimainkan sebagai aktivitas perkebunan normal.

- **Choose a Commodity** — Player dapat berinteraksi dengan Kopi, Kayu Manis, atau Sawit.
- **Kopi** — Plant → Maintain → Grow → Harvest.
- **Kayu Manis** — Maintain → Harvest → Regrowth.
- **Sawit** — Maintain → Fruit Growth → Harvest → Regrowth.
- **Sell the Harvest** — Hasil panen dapat dijual untuk memperoleh currency.
- **Use or Save Currency** — Currency dapat digunakan untuk membeli pupuk yang mempercepat growth/recovery atau disimpan untuk kebutuhan lain.
- **Repeat Freely** — Tidak ada kondisi “kebun selesai”; aktivitas dapat diulang ketika tanaman kembali siap.

**Transition:** Player dapat meninggalkan perkebunan kapan saja dan kembali ketika ingin memanen atau merawat tanaman lagi.

### Egrang

Seorang bapak tua mengomentari jalan yang rusak, berlubang, dan becek. Alih-alih memperbaiki jalan, ia menawarkan permainan masa mudanya—egrang—sebagai cara agar player tidak terkena cipratan sekaligus mendapat “latihan keseimbangan.”

- **Take the Egrang** — Player mendapatkan akses ke egrang dari area permainan.
- **Ride and Move** — Egrang digunakan sebagai rideable mobility toy dengan posisi player lebih tinggi dari berjalan biasa.
- **No Balance Simulation** — Tidak ada balance meter, random falling, damage, atau sistem keseimbangan kompleks.
- **Use Beyond the Play Area** — Egrang dapat dibawa dan digunakan selama eksplorasi.
- **Stop Anytime** — Player dapat turun kapan saja dan menggunakan egrang kembali kemudian.

**Transition:** Tidak ada win/lose condition. Player cukup berhenti menggunakan egrang dan melanjutkan eksplorasi.

### Mancing di Empang

Di sebelah empang sedang berlangsung penggusuran sebagian pemukiman, tetapi para pemancing tetap fokus pada kegiatan mereka dan menganggap keributan tersebut bukan urusan mereka. Player diajak ikut memancing sebagai aktivitas santai.

- **Use Standard Fishing** — Fishing menggunakan mekanik dasar Minecraft: Cast → Wait → Catch.
- **Custom Catch Items** — Loot ikan untuk aktivitas ini diganti menjadi Lele, Tuna, dan Hiu.
- **Absurd Rare Catch** — Hiu menjadi hasil tangkapan yang lebih jarang dan menjadi bagian dari joke aktivitas.
- **No Extra Progression** — Tidak ada custom timing system, fishing level, leaderboard, atau economy progression khusus.
- **Stay or Leave** — Player dapat terus memancing atau pergi kapan saja.

**Transition:** Tidak ada completion wajib; player kembali ke eksplorasi ketika berhenti memancing.

### Harimau Lepas

Di Jalan Utama, Zookeeper sedang makan bakso setelah mengangkut harimau dari kebun binatang. Harimaunya lepas di basement parkiran gedung sebelah, tetapi Zookeeper meminta player menanganinya karena ia tidak ingin baksonya keburu dingin.

- **Receive the Request** — NPC menjelaskan harimau lepas dan meminta player membantu.
- **Enter the Basement** — Player menuju basement parkiran dan mencari harimau.
- **Roaming Threat** — Sebelum bertemu player, harimau berkeliaran di area encounter.
- **Chase and Combat** — Saat mendeteksi player, harimau mengejar dan menyerang seperti hostile mob.
- **Defeat the Tiger** — Harimau memiliki daya tahan lebih tinggi daripada mob biasa dan harus dikalahkan.
- **Retry if Needed** — Jika player kalah, encounter dapat dicoba kembali tanpa mengulang seluruh world.

**Transition:** Setelah harimau ditangani, player dapat kembali menemui Zookeeper untuk line penutup lalu kembali mengeksplorasi kota.

### CyberWorld Mining

Di tengah sulitnya mencari pekerjaan, seorang recruiter menawarkan pekerjaan di luar pulau yang terdengar mudah dan bergaji besar. Setelah menerima tawaran, player dibawa ke kawasan pertambangan dengan tiga tingkat pulau dan sistem “jenjang karier” yang mengharuskan player membayar biaya akses untuk naik tingkat.

- **Take the Job** — Player menerima tawaran kerja dan dibawa menuju area pertambangan.
- **Start at Mining Island 1** — Player menambang resource dasar dan menukarkannya menjadi currency.
- **Upgrade Equipment** — Currency digunakan untuk meningkatkan mining equipment agar progression terasa meningkat.
- **Pay for Access** — Akses ke Mining Island 2 dan Mining Island 3 dibuka dengan membayar biaya.
- **Mine Better Resources** — Pulau dengan tier lebih tinggi menyediakan resource dengan nilai lebih tinggi.
- **Repeat the Work Loop** — Mine → Collect → Exchange → Earn → Upgrade → Pay Access → Unlock → Repeat.

**Transition:** Tidak ada ending wajib. Player dapat terus mining untuk progression atau kembali ke aktivitas lain.

## 03. Global Development

### Development Overview

Implementasi Around The Block harus menjaga enam aktivitas sebagai modul independen di dalam world yang sudah dibangun. Fokus development adalah membuat activation, gameplay loop, narrative delivery, local completion/retry, dan shared economy bekerja tanpa menambahkan architecture atau detail map yang tidak diperlukan oleh briefing.

#### Development Flow

- **Activity Ready State** — Pastikan setiap aktivitas dapat dimulai dari kondisi lokal yang bersih.
- **Narrative Delivery** — Mainkan line NPC yang relevan satu kali pada momen yang tepat sebelum atau selama aktivitas.
- **Run Local Gameplay** — Aktivasi hanya mechanic yang diperlukan oleh aktivitas tersebut.
- **Return to Exploration** — Setelah selesai atau ditinggalkan, lepaskan state lokal tanpa memengaruhi aktivitas lain.

#### Development Requirements

##### Activity Independence
- Requirement: Keenam gameplay tidak membentuk progression linear wajib.
- Requirement: Selesai atau gagal pada satu gameplay tidak boleh mengunci gameplay lain.
- Result: Player tetap bebas menjelajah dan memilih aktivitas.

##### Narrative Delivery
- Requirement: Gunakan satu NPC narrator sederhana per gameplay context; tidak diperlukan dialogue tree.
- Requirement: Voice line harus mempertahankan wording/tone approved dan tidak berubah menjadi tutorial panjang.
- Result: Premise dan humor terbaca tanpa menambah quest-system complexity.

##### Shared Economy
- Requirement: Perkebunan dan CyberWorld Mining dapat menggunakan shared currency.
- Requirement: Egrang, Fishing, Benteng Martello, dan Harimau Lepas tidak wajib menghasilkan currency.
- Result: Economy menghubungkan aktivitas yang memang membutuhkan progression tanpa memaksa semua gameplay menjadi grind.

##### Existing Map Boundary
- Requirement: Gunakan layout map yang sudah ada sebagai authority.
- Requirement: Jangan menambahkan redesign map, exact coordinates, atau as-built setup detail ke PRD.
- Result: Dokumen tetap menjadi gameplay briefing dan production requirement, bukan forensic implementation document.

#### Important Development Notes

- **Narration Is Context, Not Tutorial** — Voice membuka premise dan tone; instruksi gameplay hanya muncul ketika benar-benar diperlukan.
- **Local State Only** — Runtime state satu gameplay tidak boleh mengubah gameplay lain secara tidak sengaja.
- **Reuse Existing Systems Where Possible** — Vanilla fishing dan simple hostile-mob behavior dipertahankan bila sudah cukup.
- **No Unapproved Complexity** — Jangan menambahkan skill tree, crafting system, custom balance simulation, dialogue branching, atau framework baru tanpa kebutuhan yang sudah disetujui.

### Game System

Shared system hanya perlu mengetahui aktivitas mana yang sedang aktif untuk player, narrative state yang sudah diputar, shared currency bila digunakan, dan progression lokal yang memang persist.

#### Development Flow

- **Discover** — Player mendekati activity/NPC.
- **Narrate** — Mainkan narrative yang relevan.
- **Activate** — Berikan akses ke mechanic atau encounter.
- **Release** — Selesaikan state lokal dan kembalikan player ke eksplorasi bebas.

#### Development Requirements

##### Narrative State
- Requirement: Jangan memutar opening narrative berulang-ulang selama satu interaction/session pendek.
- Requirement: Completion line hanya muncul setelah kondisi lokalnya terpenuhi.
- Result: Voice terasa disengaja dan tidak spam.

##### Activity State
- Requirement: Aktivitas repeatable harus dapat kembali ke kondisi playable.
- Requirement: PvP match dan Tiger encounter memiliki local finish/retry state yang jelas.
- Result: Aktivitas dapat digunakan kembali tanpa mengubah struktur world.

##### Economy State
- Requirement: Currency Farming/Mining disimpan secara konsisten ketika player meninggalkan area.
- Requirement: Pembelian pupuk, equipment upgrade, dan paid access hanya mengurangi currency setelah transaksi valid.
- Result: Progression ekonomi dapat ditinggalkan dan dilanjutkan.

##### Player Freedom
- Requirement: Aktivitas leisure/free-play tidak memiliki forced completion.
- Result: Egrang dan Fishing tetap terasa sebagai aktivitas dunia, bukan objective wajib.

#### Important Development Notes

- **No Global Campaign Gate** — Tidak ada flag “complete all six” yang dibutuhkan untuk bermain.
- **Narrative Replay Control** — Opening line boleh memiliki cooldown/replay rule sederhana, tetapi tidak perlu dialogue-state graph.
- **Economy Persistence** — Farming/Mining progression tidak hilang hanya karena player mencoba gameplay lain.
- **Match Ownership** — Benteng Martello hanya menjalankan match ketika jumlah participant yang dibutuhkan tersedia.

### Data and Reset

Data dibatasi pada state yang benar-benar dibutuhkan untuk kelanjutan aktivitas. Tidak ada kebutuhan telemetry/scoring platform yang ditetapkan dalam briefing ini.

#### Development Flow

- **Store Local Progress** — Simpan currency dan progression yang memang perlu bertahan.
- **Clear Temporary State** — Bersihkan entity/projectile/temp state setelah match atau encounter selesai.
- **Restore Repeatable Gameplay** — Kembalikan tanaman, fishing availability, egrang, dan encounter ke state yang dapat dimainkan lagi sesuai mechanic.
- **Resume Freely** — Player dapat kembali ke aktivitas tanpa menjalankan campaign reset.

#### Development Requirements

##### Persistent State
- Requirement: Simpan shared currency, mining access, mining equipment progression, dan farming growth/recovery state bila sistem yang dipakai memang membutuhkan persistensi.
- Result: Aktivitas progression dapat dilanjutkan.

##### Temporary State
- Requirement: Projectile, match state, combat entity, dan temporary interaction state tidak boleh bocor ke aktivitas lain setelah selesai.
- Result: World tetap stabil setelah aktivitas berulang.

##### Retry
- Requirement: Tiger encounter dapat diulang setelah player kalah.
- Requirement: Benteng Martello memulai match baru dari state kapal/PvP yang bersih.
- Result: Failure lokal tidak merusak world.

##### No Score Requirement
- Requirement: Jangan invent scoring system untuk gameplay yang tidak memiliki scoring approved.
- Result: Briefing tetap sesuai scope.

#### Important Development Notes

- **Persist Only What Matters** — Jangan membuat data layer baru untuk state yang bisa direstore sederhana.
- **No As-Built Coordinates** — Spawn/trigger exact locator tetap di luar canonical PRD.
- **Safe Repeatability** — Repeatable activity harus dapat kembali dimainkan tanpa manual world repair.
- **Do Not Infer Rewards** — Reward ekonomi hanya digunakan ketika sudah disetujui oleh gameplay.

### Gameplay Development

Setiap gameplay mengikuti lifecycle sederhana: narrative → activation → gameplay → local result/retry → return to exploration.

#### Development Flow

- **Prepare** — Pastikan activity state dapat digunakan.
- **Introduce** — Mainkan NPC narrative.
- **Play** — Jalankan mechanic inti.
- **Resolve** — Selesaikan local result lalu lepas player kembali ke world.

#### Development Requirements

##### Activation
- Requirement: Interaction NPC atau activity entry memicu narrative/activation yang relevan.
- Result: Player memahami konteks sebelum bermain.

##### Gameplay Ownership
- Requirement: Hanya mechanic yang disetujui untuk tiap aktivitas yang dijalankan.
- Result: Scope tidak berkembang menjadi minigame tambahan.

##### Completion / Exit
- Requirement: Competitive/PvE activity menggunakan local end condition; leisure activity dapat ditinggalkan kapan saja.
- Result: Setiap activity memiliki exit behavior sesuai identitasnya.

##### Reuse
- Requirement: Setelah selesai/ditinggalkan, activity kembali ke state yang dapat digunakan lagi sesuai kebutuhan.
- Result: World mendukung aktivitas optional yang berulang.

#### Important Development Notes

- **Keep It Lightweight** — Implementasi harus memilih mechanic sederhana yang memenuhi experience.
- **Voice Is Part of Gameplay Identity** — Approved narration tidak boleh dihilangkan ketika gameplay dibuat.
- **No Map Redesign** — Hanya kebutuhan functional/readability yang boleh memengaruhi existing area.
- **Scope by Activity** — Setiap gameplay dikembangkan sebagai bounded module.

## 04. Benteng Martello

### Gameplay Overview

**Context:** Player menemukan atraksi Benteng Martello yang menawarkan pengalaman “merasakan hidup di zaman kolonial” dan mengajak minimal satu player lain untuk ikut.

**Main Objective:** Bertahan melalui Naval Combat dan Island PvP sampai menjadi Last Player Standing.

**Result:** Satu player dinyatakan sebagai pemenang Benteng Martello PvP.

#### Gameplay Information

- **Game Purpose:** Memberikan competitive PvP dua fase dengan perpindahan dari pertempuran kapal ke pertarungan pulau.
- **Gameplay Time:** Naval phase memiliki DeathTime; total match time belum ditetapkan.
- **Starting Condition:** Sekitar 2–6 participant masuk ke match dan setiap player memulai di kapal masing-masing.
- **End Condition:** Hanya satu player yang masih bertahan.
- **Fail Condition:** Player tereliminasi dari PvP; kapal hancur bukan eliminasi langsung.
- **Scoring Criteria:** Tidak ada scoring formula approved; hasil utama adalah winner/loser match.

#### Gameplay Flow

- **Join the Attraction** — Dengarkan premise wisata sejarah dan kumpulkan participant.
- **Fight from the Ships** — Gunakan meriam kapal untuk menekan atau menghancurkan kapal lawan.
- **Move Toward the Island** — Kapal hancur atau DeathTime memindahkan fokus dari laut ke darat.
- **Use Shore Pressure** — Survivor di pulau dapat memakai meriam pantai untuk menyerang kapal yang masih aktif.
- **Finish the PvP** — Bertarung di arena pulau sampai tersisa satu player.

### Level Design

Gunakan existing Benteng Martello area tanpa redesign. Kebutuhan build hanya memastikan area yang sudah ada dapat membaca kapal di perairan, jalur menuju pulau, meriam pantai, arena terbuka, dan air sebagai hazard.

#### Design Flow

- **Ship Start** — Area kapal terpisah dan terbaca untuk participant.
- **Water Transition** — Perairan memungkinkan perpindahan menuju pulau dengan risiko hiu.
- **Shore Cannon Line** — Meriam pantai menghadap area perairan yang relevan.
- **Open PvP Arena** — Pulau menyediakan ruang akhir untuk Last Player Standing.

#### Build Requirements

- **Existing Water Combat Area** — Harus cukup untuk beberapa kapal bergerak dan saling menembak.
- **Island Access** — Player dari kapal yang hancur masih memiliki jalur gameplay menuju pulau.
- **Shore Cannons** — Posisi meriam memungkinkan tekanan terhadap kapal yang masih aktif.
- **Open Arena** — Final PvP menggunakan satu arena terbuka tanpa redesign map baru.

#### Important Build Notes

- **Existing Map First** — Tidak ada kebutuhan layout baru.
- **Water Is Playable Risk** — Air bukan instant-death boundary.
- **Shark Readability** — Ancaman hiu harus terlihat/terbaca ketika player berada di air.
- **Two-Phase Readability** — Player harus memahami bahwa match akhirnya berpindah ke pulau.

### Developer

Implementasikan match 2–6 player (estimasi), kapal/meriam, ship damage, DeathTime, shore cannon, shark hazard, player elimination, dan Last Player Standing tanpa menambah scoring system baru.

#### Development Flow

- **Match Setup** — Assign participant dan kapal.
- **Naval Combat** — Jalankan ship movement, cannon fire, dan ship damage.
- **Forced Transition** — Gunakan ship destruction/DeathTime untuk mengakhiri naval dominance.
- **Island Resolution** — Track eliminations sampai tersisa satu winner.

#### Development Requirements

- Kapal hancur tidak langsung mengeliminasi player.
- DeathTime mengakhiri penggunaan kapal yang masih tersisa.
- Hiu menyerang player yang berada di air.
- Meriam pantai dapat menargetkan kapal aktif.
- Match selesai ketika hanya satu player tersisa.

#### Important Development Notes

- **Participant Estimate** — 2–6 masih estimasi dan tidak boleh diperlakukan sebagai platform cap final.
- **No Ship Camping** — DeathTime wajib mendorong perpindahan fase.
- **One Winner** — Result utama adalah Last Player Standing.
- **Clean Match Reset** — Kapal, projectiles, sharks/match state, dan player combat state harus siap untuk match berikutnya.

## 05. Perkebunan

### Gameplay Overview

**Context:** Player bertemu NPC perkebunan yang membanggakan tren menjadi petani dan memiliki antusiasme khusus terhadap sawit.

**Main Objective:** Pilih komoditas, rawat/panen, lalu jual hasil untuk memperoleh currency.

**Result:** Player mendapatkan hasil panen/currency dan dapat menggunakan pupuk atau meninggalkan perkebunan.

#### Gameplay Information

- **Game Purpose:** Memberikan farming loop santai dengan tiga komoditas yang memiliki pola interaction berbeda.
- **Gameplay Time:** Tidak ada batas waktu; growth/recovery berjalan sesuai sistem tanaman.
- **Starting Condition:** Tanaman berada pada state yang dapat ditanam, dirawat, atau dipanen.
- **End Condition:** Tidak ada completion wajib; satu loop dapat dianggap selesai setelah hasil dipanen/dijual.
- **Fail Condition:** Tidak ada fail state berat.
- **Scoring Criteria:** Tidak ada score; progression berupa harvest dan currency.

#### Gameplay Flow

- **Hear the Farming Pitch** — NPC memperkenalkan tren bertani.
- **Choose a Commodity** — Kopi, Kayu Manis, atau Sawit.
- **Care and Grow** — Lakukan interaction sesuai komoditas.
- **Harvest and Sell** — Ambil hasil lalu jual untuk currency.
- **Invest or Leave** — Beli pupuk untuk growth/recovery lebih cepat atau simpan uang.

### Level Design

Existing plantation layout dipertahankan. Hanya perlu memastikan ketiga komoditas, titik interaction, dan area jual/pupuk mudah dikenali.

#### Design Flow

- **Narrative Entry** — NPC terbaca dari jalur player.
- **Three Commodity Areas** — Kopi, Kayu Manis, dan Sawit dapat dibedakan.
- **Harvest Readability** — State siap panen terbaca secara visual.
- **Sell / Fertilizer Access** — Player dapat menemukan fungsi ekonomi tanpa area baru.

#### Build Requirements

- **Coffee Area** — Mendukung plant/growth/harvest states.
- **Cinnamon Area** — Mendukung maintain/harvest/regrowth states.
- **Palm Oil Area** — Mendukung maintain/fruit/harvest/regrowth states.
- **Economy Interaction** — Existing area menyediakan interaction untuk menjual hasil dan membeli pupuk.

#### Important Build Notes

- **No Map Redesign** — Layout perkebunan sudah dianggap final.
- **Commodity Identity** — Tiga tanaman tidak terasa sebagai interaction yang sama dengan skin berbeda.
- **Sawit Satire Stays Narrative** — Tidak perlu mechanic khusus untuk satire.
- **Readable Harvest State** — Player harus tahu kapan tanaman dapat dipanen.

### Developer

Implementasikan tiga crop loops, harvest item, sale/currency, fertilizer acceleration, dan repeatable regrowth tanpa farming framework tambahan.

#### Development Flow

- **Initialize Crop State** — Load plant/growth/harvest state.
- **Run Crop Interaction** — Tangani plant/maintain/harvest sesuai komoditas.
- **Sell / Spend** — Tukarkan hasil dan proses pembelian pupuk.
- **Regrow / Persist** — Jalankan recovery/growth dan simpan state yang diperlukan.

#### Development Requirements

- Kopi menggunakan Plant → Maintain → Grow → Harvest.
- Kayu Manis menggunakan Maintain → Harvest → Regrowth.
- Sawit menggunakan Maintain → Fruit Growth → Harvest → Regrowth.
- Pupuk mempercepat growth/recovery.
- Currency dapat disimpan dan digunakan di luar satu kunjungan ke kebun.

#### Important Development Notes

- **No Forced Completion** — Player dapat hanya melakukan satu interaction lalu pergi.
- **Shared Currency** — Economy harus konsisten dengan CyberWorld Mining.
- **No Permanent Crop Loss** — Harvest tidak menghapus akses komoditas secara permanen.
- **Narrative Is Separate from Crop Logic** — Satire tidak memerlukan logic khusus.

## 06. Egrang

### Gameplay Overview

**Context:** Bapak tua menawarkan egrang setelah mengomentari jalan yang rusak dan becek.

**Main Objective:** Gunakan egrang sebagai permainan tradisional dan alat mobility bebas.

**Result:** Player dapat bergerak dengan egrang lalu turun kapan saja.

#### Gameplay Information

- **Game Purpose:** Memberikan free-play traditional activity yang mudah diimplementasikan.
- **Gameplay Time:** Tidak ada batas waktu.
- **Starting Condition:** Egrang tersedia untuk digunakan.
- **End Condition:** Tidak ada completion; player berhenti dengan dismount.
- **Fail Condition:** Tidak ada fail state.
- **Scoring Criteria:** Tidak ada score atau currency.

#### Gameplay Flow

- **Hear the Old Man** — Dapatkan premise jalan rusak.
- **Take the Egrang** — Aktivasi/ambil egrang.
- **Ride** — Bergerak pada posisi lebih tinggi.
- **Explore** — Gunakan di area permainan atau dibawa ke area lain.
- **Dismount** — Turun dan lanjutkan eksplorasi.

### Level Design

Tidak ada obstacle course wajib. Existing jalan rusak dan area permainan cukup menjadi konteks penggunaan egrang.

#### Design Flow

- **Old Man / Egrang Point** — Narasi dan egrang mudah ditemukan.
- **Broken Road Context** — Jalan rusak terlihat sebagai sumber joke.
- **Free Movement** — Route tidak mengunci egrang pada satu petak.
- **Return to Normal Movement** — Dismount dapat dilakukan tanpa area khusus.

#### Build Requirements

- Existing area harus memberi ruang untuk mount/dismount.
- Jalan rusak/becek tetap terbaca sebagai context.
- Tidak perlu arena kompetisi atau obstacle mandatory.
- Egrang dapat dibawa keluar area permainan.

#### Important Build Notes

- **No Balance Mechanic** — Jangan membangun level yang mengandalkan sistem jatuh yang tidak ada.
- **No Forced Route** — Egrang adalah world toy.
- **Keep Movement Readable** — Tinggi rider tidak boleh membuat navigasi dasar membingungkan.
- **Existing Map Only** — Tidak ada redesign.

### Developer

Gunakan rideable entity/equipment sederhana untuk egrang; tidak diperlukan simulation keseimbangan.

#### Development Flow

- **Make Available** — Egrang dapat diakses player.
- **Mount** — Player masuk ke rideable state.
- **Move** — Gunakan movement sederhana.
- **Dismount / Reuse** — Player turun dan egrang dapat dipakai lagi.

#### Development Requirements

- Tidak ada balance meter, random fall, damage, timer, leaderboard, atau progression.
- Posisi player lebih tinggi daripada walking normal.
- Egrang dapat digunakan di luar area awal.
- Dismount mengembalikan player ke movement normal.

#### Important Development Notes

- **Implementation Simplicity First**
- **No Fake Physics Requirement**
- **Reusable Equipment**
- **No Economy Dependency**

## 07. Mancing di Empang

### Gameplay Overview

**Context:** Penggusuran berlangsung di sebelah empang sementara pemancing memilih tetap fokus pada pancingan.

**Main Objective:** Memancing menggunakan mekanik dasar Minecraft dan mendapatkan Lele, Tuna, atau Hiu.

**Result:** Player menyimpan hasil tangkapan atau berhenti memancing kapan saja.

#### Gameplay Information

- **Game Purpose:** Memberikan leisure activity dengan joke loot yang absurd.
- **Gameplay Time:** Tidak ada batas waktu.
- **Starting Condition:** Player memiliki akses ke fishing rod dan empang.
- **End Condition:** Tidak ada completion wajib.
- **Fail Condition:** Tidak ada fail state berat; fishing mengikuti behavior dasar Minecraft.
- **Scoring Criteria:** Tidak ada score/progression khusus.

#### Gameplay Flow

- **Hear the Fisherman** — Dapatkan premise empang/penggusuran.
- **Cast** — Gunakan fishing rod Minecraft biasa.
- **Wait** — Tunggu bite seperti vanilla fishing.
- **Catch** — Terima Lele, Tuna, atau Hiu.
- **Continue or Leave** — Ulangi atau kembali ke eksplorasi.

### Level Design

Existing empang dan situasi penggusuran menjadi context visual. Tidak diperlukan fishing arena baru.

#### Design Flow

- **Narrative Spot** — Pemancing/NPC terbaca.
- **Fishing Edge** — Tepi empang dapat digunakan dengan vanilla fishing interaction.
- **Background Context** — Penggusuran terlihat tanpa menghalangi fishing.
- **Free Exit** — Player dapat pergi kapan saja.

#### Build Requirements

- Fishing spot mendukung mechanic vanilla.
- Penggusuran tetap menjadi background story, bukan hazard gameplay.
- Tidak diperlukan custom obstacle/progression area.
- Fishing rod tidak perlu custom model bila vanilla rod digunakan.

#### Important Build Notes

- **Vanilla Mechanic First**
- **Custom Loot Only**
- **No Economy Requirement**
- **Satire Is Narrative/Environment**

### Developer

Pertahankan vanilla fishing behavior dan ganti loot relevant menjadi Lele, Tuna, dan Hiu.

#### Development Flow

- **Enable Fishing**
- **Detect Valid Catch**
- **Replace/Select Custom Fish Loot**
- **Return to Repeatable Fishing State**

#### Development Requirements

- Cast/wait/catch mengikuti mechanic dasar Minecraft.
- Custom catch set adalah Lele, Tuna, dan Hiu.
- Hiu lebih jarang daripada tangkapan biasa.
- Tidak ada fishing level, leaderboard, atau custom timing framework.

#### Important Development Notes

- **Do Not Rebuild Fishing**
- **Hiu Is Intentional Absurdity**
- **No Forced Completion**
- **Loot Reset Must Remain Repeatable**

## 08. Harimau Lepas

### Gameplay Overview

**Context:** Zookeeper makan bakso di Jalan Utama sementara harimau yang dibawanya lepas di basement parkiran.

**Main Objective:** Temukan dan kalahkan harimau di basement.

**Result:** Harimau ditangani, line penutup Zookeeper dapat diputar, dan player kembali ke eksplorasi.

#### Gameplay Information

- **Game Purpose:** Memberikan short PvE encounter dengan premise komedi.
- **Gameplay Time:** Tidak ada target waktu approved.
- **Starting Condition:** Encounter belum selesai dan harimau tersedia di basement.
- **End Condition:** Harimau dikalahkan.
- **Fail Condition:** Player kalah dalam combat; encounter dapat dicoba lagi.
- **Scoring Criteria:** Tidak ada score atau currency reward approved.

#### Gameplay Flow

- **Meet the Zookeeper** — Dengarkan request.
- **Find the Tiger** — Masuk basement dan cari target.
- **Trigger the Chase** — Harimau mendeteksi player.
- **Fight** — Hindari serangan dan kurangi health harimau.
- **Resolve** — Kalahkan harimau lalu kembali ke Zookeeper bila diinginkan.

### Level Design

Existing basement dipertahankan. Area hanya perlu mendukung roaming, detection, chase, dan combat tanpa redesign.

#### Design Flow

- **Narrative Location** — Zookeeper berada di jalan sebagai entry point.
- **Basement Entry** — Route ke encounter sudah ada.
- **Roaming Space** — Harimau dapat bergerak tanpa tersangkut.
- **Combat Space** — Player memiliki ruang wajar untuk encounter.

#### Build Requirements

- Basement existing dapat menampung roaming/chase.
- Tidak perlu escape-path puzzle kompleks.
- Route keluar kota hanya menjadi story stakes, bukan fail-path simulation.
- Zookeeper tetap terpisah dari combat area.

#### Important Build Notes

- **Short Encounter**
- **No Boss Multi-Phase**
- **Readable Tiger Movement**
- **Retry Without World Restart**

### Developer

Gunakan hostile-mob style behavior: roam → detect → chase → attack → defeat, dengan health/damage yang cukup untuk terasa sebagai encounter khusus.

#### Development Flow

- **Spawn / Roam**
- **Detect / Chase**
- **Combat**
- **Defeat / Retry Reset**

#### Development Requirements

- Harimau roaming sebelum aggro.
- Setelah mendeteksi player, harimau mengejar dan menyerang.
- Harimau lebih tahan daripada mob normal, tanpa multi-phase mechanic.
- Player death tidak menutup encounter permanen.
- Completion line hanya diputar setelah defeat valid.

#### Important Development Notes

- **No Complex Escape AI**
- **No Currency Reward Invented**
- **Narrative Tone Must Stay Calm/Absurd**
- **Reset Tiger State for Retry**

## 09. CyberWorld Mining

### Gameplay Overview

**Context:** Recruiter menawarkan pekerjaan di luar pulau kepada player yang sedang mencari kerja dan menjanjikan pekerjaan mudah dengan gaji besar.

**Main Objective:** Menambang resource, menghasilkan currency, upgrade equipment, dan membuka akses ke tiga tier pulau tambang.

**Result:** Player meningkatkan mining progression dan dapat melanjutkan kerja atau kembali ke world.

#### Gameplay Information

- **Game Purpose:** Memberikan repeatable economy/progression loop.
- **Gameplay Time:** Tidak ada total limit.
- **Starting Condition:** Player menerima pekerjaan dan memiliki akses ke Mining Island 1.
- **End Condition:** Tidak ada ending wajib; progression tertinggi adalah akses ke Mining Island 3.
- **Fail Condition:** Tidak ada fail state utama yang disetujui.
- **Scoring Criteria:** Tidak ada score; progression dinilai dari currency, equipment, dan access tier.

#### Gameplay Flow

- **Take the Offer** — Dengarkan recruiter dan masuk ke pekerjaan.
- **Mine Island 1** — Kumpulkan resource dasar.
- **Earn and Upgrade** — Tukar resource menjadi currency dan tingkatkan equipment.
- **Pay to Move Up** — Bayar biaya akses untuk Island 2 lalu Island 3.
- **Repeat at Higher Value** — Tambang resource yang lebih bernilai dan lanjutkan progression.

### Level Design

Tiga island mining dianggap sudah tersedia. PRD hanya membutuhkan perbedaan fungsi/tier agar progression terbaca.

#### Design Flow

- **Recruitment Point**
- **Mining Island 1 — Entry Tier**
- **Mining Island 2 — Paid Mid Tier**
- **Mining Island 3 — Paid High Tier**

#### Build Requirements

- Masing-masing island dapat dibedakan sebagai tier progression.
- Access ke Island 2/3 dapat dikunci sampai pembayaran valid.
- Resource yang lebih bernilai tersedia pada tier lebih tinggi.
- Tidak ada kebutuhan redesign layout island dalam scope ini.

#### Important Build Notes

- **Three Tiers Stay Clear**
- **Paid Access Is Part of the Joke and Progression**
- **Existing Map Boundary**
- **No Extra Skill Tree**

### Developer

Implementasikan mining resource, exchange currency, equipment upgrade, dan paid island access sebagai loop sederhana dan repeatable.

#### Development Flow

- **Mine**
- **Exchange**
- **Upgrade / Pay**
- **Unlock / Repeat**

#### Development Requirements

- Island 1 tersedia setelah pekerjaan diterima.
- Resource dapat ditukar menjadi shared currency.
- Mining equipment dapat di-upgrade.
- Island 2 dan Island 3 memerlukan biaya akses.
- Higher-tier island memberikan resource bernilai lebih tinggi.
- Progression dapat ditinggalkan dan dilanjutkan kembali.

#### Important Development Notes

- **Shared Currency with Farming**
- **No Crafting System Required**
- **Access Payment Must Be Validated**
- **Do Not Invent Resource Names Until Approved**
