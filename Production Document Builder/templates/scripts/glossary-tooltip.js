(() => {
  const glossary = {"docks":[{"key":"docks-0","label":{"en":"Assigned Arena","id":"Assigned Arena"},"definition":{"en":"The isolated gameplay area used by the current player or session.","id":"Area gameplay terpisah yang digunakan oleh player atau sesi saat ini."},"aliases":{"en":["Assigned Arena"],"id":["Assigned Arena"]}},{"key":"docks-1","label":{"en":"Objective Marker","id":"Objective Marker"},"definition":{"en":"The visible marker that shows the next required tutorial action or destination.","id":"Penanda yang menunjukkan tindakan atau tujuan tutorial wajib berikutnya."},"aliases":{"en":["Objective Marker"],"id":["Objective Marker"]}},{"key":"docks-2","label":{"en":"Broken Gangway","id":"Broken Gangway"},"definition":{"en":"The damaged dock crossing repaired with the Repair Plate.","id":"Jalur dermaga rusak yang diperbaiki menggunakan Repair Plate."},"aliases":{"en":["Broken Gangway"],"id":["Broken Gangway"]}},{"key":"docks-3","label":{"en":"Repair Plate","id":"Repair Plate"},"definition":{"en":"The protected tutorial item used once to repair the Broken Gangway.","id":"Item tutorial terlindungi yang digunakan satu kali untuk memperbaiki Broken Gangway."},"aliases":{"en":["Repair Plate"],"id":["Repair Plate"]}},{"key":"docks-4","label":{"en":"Crane Gate","id":"Crane Gate"},"definition":{"en":"The dock gate opened by the marked lever after the gangway is repaired.","id":"Gerbang dermaga yang dibuka melalui lever bertanda setelah gangway diperbaiki."},"aliases":{"en":["Crane Gate"],"id":["Crane Gate"]}},{"key":"docks-5","label":{"en":"Power Component","id":"Power Component"},"definition":{"en":"The protected component carried from the Crane Gate area to the Power Terminal.","id":"Komponen terlindungi yang dibawa dari area Crane Gate menuju Power Terminal."},"aliases":{"en":["Power Component"],"id":["Power Component"]}},{"key":"docks-6","label":{"en":"Power Terminal","id":"Power Terminal"},"definition":{"en":"The machine that accepts the Power Component and restores dock power.","id":"Mesin yang menerima Power Component dan memulihkan tenaga dermaga."},"aliases":{"en":["Power Terminal"],"id":["Power Terminal"]}},{"key":"docks-7","label":{"en":"Brann","id":"Brann"},"definition":{"en":"The guide who briefs the player and communicates through the Steampunk Communicator.","id":"Pemandu yang memberi briefing dan berkomunikasi melalui Steampunk Communicator."},"aliases":{"en":["Brann"],"id":["Brann"]}},{"key":"docks-8","label":{"en":"Steampunk Communicator","id":"Steampunk Communicator"},"definition":{"en":"The fixed player item used for Brann messages, hints, emergency travel, and Exit when available.","id":"Item tetap milik player untuk pesan Brann, hint, perjalanan darurat, dan Exit saat tersedia."},"aliases":{"en":["Steampunk Communicator"],"id":["Steampunk Communicator"]}}],"quarry":[{"key":"quarry-0","label":{"en":"Forge Hub","id":"Forge Hub"},"definition":{"en":"The central building that connects The Forge, the Automatic Lift, the caves, and the route to The Ascent.","id":"Bangunan pusat yang menghubungkan The Forge, Automatic Lift, cave, dan jalur menuju The Ascent."},"aliases":{"en":["Forge Hub"],"id":["Forge Hub"]}},{"key":"quarry-1","label":{"en":"The Forge","id":"The Forge"},"definition":{"en":"The machine that processes material from the active cave and creates the Beacon Core after Gold is complete.","id":"Mesin yang memproses material dari cave aktif dan membuat Beacon Core setelah tahap Gold selesai."},"aliases":{"en":["The Forge"],"id":["The Forge"]}},{"key":"quarry-2","label":{"en":"Automatic Lift","id":"Automatic Lift"},"definition":{"en":"The single lift connecting the Forge Hub with Bronze, Silver, and Gold Cave.","id":"Satu lift yang menghubungkan Forge Hub dengan Bronze Cave, Silver Cave, dan Gold Cave."},"aliases":{"en":["Automatic Lift"],"id":["Automatic Lift"]}},{"key":"quarry-3","label":{"en":"Quarry Pickaxe","id":"Quarry Pickaxe"},"definition":{"en":"The protected pickaxe used only to mine ore in the active cave during The Quarry.","id":"Pickaxe terlindungi yang hanya digunakan untuk menambang ore di cave aktif selama The Quarry."},"aliases":{"en":["Quarry Pickaxe"],"id":["Quarry Pickaxe"]}},{"key":"quarry-4","label":{"en":"Required Ore","id":"Required Ore"},"definition":{"en":"The minimum ore that must be processed before the next cave can open.","id":"Jumlah minimum ore yang harus diproses sebelum cave berikutnya dapat dibuka."},"aliases":{"en":["Required Ore"],"id":["Required Ore"]}},{"key":"quarry-5","label":{"en":"Surplus Ore","id":"Surplus Ore"},"definition":{"en":"Optional ore beyond the required amount. Only surplus processed through The Forge adds Surplus Score.","id":"Ore tambahan di luar jumlah wajib. Hanya surplus yang diproses melalui The Forge yang menambah Surplus Score."},"aliases":{"en":["Surplus Ore"],"id":["Surplus Ore"]}},{"key":"quarry-6","label":{"en":"Beacon Core","id":"Beacon Core"},"definition":{"en":"The protected power source created in The Quarry and carried to the Main Beacon.","id":"Sumber tenaga terlindungi yang dibuat di The Quarry dan dibawa menuju Main Beacon."},"aliases":{"en":["Beacon Core"],"id":["Beacon Core"]}},{"key":"quarry-7","label":{"en":"Quarry Score","id":"Quarry Score"},"definition":{"en":"The Objective 1 score made from 80% Time Score and 20% Surplus Score.","id":"Nilai Objective 1 yang berasal dari 80% Time Score dan 20% Surplus Score."},"aliases":{"en":["Quarry Score"],"id":["Quarry Score"]}},{"key":"quarry-8","label":{"en":"Time Score","id":"Time Score"},"definition":{"en":"The score based on completion time. Nine minutes is standard; faster adds score and slower reduces score.","id":"Nilai berdasarkan waktu penyelesaian. Sembilan menit adalah standar; lebih cepat menambah nilai dan lebih lambat mengurangi nilai."},"aliases":{"en":["Time Score"],"id":["Time Score"]}},{"key":"quarry-9","label":{"en":"Surplus Score","id":"Surplus Score"},"definition":{"en":"The score based on processed Surplus Ore. No processed surplus gives no Surplus Score.","id":"Nilai berdasarkan Surplus Ore yang diproses. Tanpa surplus yang diproses, tidak ada Surplus Score."},"aliases":{"en":["Surplus Score"],"id":["Surplus Score"]}}],"ascent":[{"key":"ascent-0","label":{"en":"Beacon Core","id":"Beacon Core"},"definition":{"en":"The protected power source carried from The Quarry to the Main Beacon.","id":"Sumber tenaga terlindungi yang dibawa dari The Quarry menuju Main Beacon."},"aliases":{"en":["Beacon Core"],"id":["Beacon Core"]}},{"key":"ascent-1","label":{"en":"Checkpoint","id":"Checkpoint"},"definition":{"en":"One of four ordered route stages that defines the active hazard and recovery location.","id":"Satu dari empat tahap rute berurutan yang menentukan hazard aktif dan lokasi kembali."},"aliases":{"en":["Checkpoint"],"id":["Checkpoint"]}},{"key":"ascent-2","label":{"en":"Tutorial Fall","id":"Tutorial Fall"},"definition":{"en":"The scripted safe fall at Checkpoint 1. It is recorded but never affects score or assistance.","id":"Jatuh aman yang sudah diatur pada Checkpoint 1. Kejadian ini dicatat tetapi tidak memengaruhi score atau bantuan."},"aliases":{"en":["Tutorial Fall"],"id":["Tutorial Fall"]}},{"key":"ascent-3","label":{"en":"Real Fall","id":"Real Fall"},"definition":{"en":"A non-tutorial fall counted once for scoring and assistance before the player returns to a Safe Landing.","id":"Jatuh di luar tutorial yang dihitung satu kali untuk scoring dan bantuan sebelum player kembali ke Safe Landing."},"aliases":{"en":["Real Fall"],"id":["Real Fall"]}},{"key":"ascent-4","label":{"en":"Safe Landing","id":"Safe Landing"},"definition":{"en":"The protected recovery area used after a Real Fall or avalanche.","id":"Area aman yang digunakan untuk mengembalikan player setelah Real Fall atau avalanche."},"aliases":{"en":["Safe Landing"],"id":["Safe Landing"]}},{"key":"ascent-5","label":{"en":"Faithless Stone","id":"Faithless Stone"},"definition":{"en":"A marked unstable block that falls after its warning during The Ascent.","id":"Block tidak stabil yang telah ditandai dan jatuh setelah peringatannya selama The Ascent."},"aliases":{"en":["Faithless Stone"],"id":["Faithless Stone"]}},{"key":"ascent-6","label":{"en":"Request Hint","id":"Request Hint"},"definition":{"en":"The Communicator option that highlights the safer route for the active Checkpoint.","id":"Opsi Communicator yang menyorot jalur lebih aman pada Checkpoint aktif."},"aliases":{"en":["Request Hint"],"id":["Request Hint"]}},{"key":"ascent-7","label":{"en":"Signal Horn","id":"Signal Horn"},"definition":{"en":"The standard summit interaction used to complete The Ascent.","id":"Interaksi standar di summit untuk menyelesaikan The Ascent."},"aliases":{"en":["Signal Horn"],"id":["Signal Horn"]}},{"key":"ascent-8","label":{"en":"Emergency Air Balloon","id":"Emergency Air Balloon"},"definition":{"en":"The assisted summit route unlocked after repeated Real Falls or all three hints.","id":"Jalur bantuan menuju summit yang terbuka setelah Real Fall berulang atau seluruh tiga hint digunakan."},"aliases":{"en":["Emergency Air Balloon"],"id":["Emergency Air Balloon"]}},{"key":"ascent-9","label":{"en":"Ascent Score","id":"Ascent Score"},"definition":{"en":"The Objective 2 score made from Fall Score, Hint Score, and Completion Route Score.","id":"Nilai Objective 2 yang berasal dari Fall Score, Hint Score, dan Completion Route Score."},"aliases":{"en":["Ascent Score"],"id":["Ascent Score"]}},{"key":"ascent-10","label":{"en":"Fall Score","id":"Fall Score"},"definition":{"en":"The score based on Real Falls. Tutorial Fall is excluded.","id":"Nilai berdasarkan Real Fall. Tutorial Fall tidak dihitung."},"aliases":{"en":["Fall Score"],"id":["Fall Score"]}},{"key":"ascent-11","label":{"en":"Hint Score","id":"Hint Score"},"definition":{"en":"The score based on how many of the three available hints are used.","id":"Nilai berdasarkan jumlah hint yang digunakan dari tiga hint yang tersedia."},"aliases":{"en":["Hint Score"],"id":["Hint Score"]}},{"key":"ascent-12","label":{"en":"Completion Route Score","id":"Completion Route Score"},"definition":{"en":"The score based on whether the player finishes through the Signal Horn or Emergency Air Balloon.","id":"Nilai berdasarkan jalur penyelesaian melalui Signal Horn atau Emergency Air Balloon."},"aliases":{"en":["Completion Route Score"],"id":["Completion Route Score"]}}],"beacon":[{"key":"beacon-0","label":{"en":"Beacon Core","id":"Beacon Core"},"definition":{"en":"The protected power source used by the Repair Machines and installed in the Main Beacon.","id":"Sumber tenaga terlindungi yang digunakan oleh Repair Machines dan dipasang pada Main Beacon."},"aliases":{"en":["Beacon Core"],"id":["Beacon Core"]}},{"key":"beacon-1","label":{"en":"Repair Machines","id":"Repair Machines"},"definition":{"en":"The three machines that produce the materials required by the Ghost Scaffold.","id":"Tiga mesin yang menghasilkan material yang dibutuhkan oleh Ghost Scaffold."},"aliases":{"en":["Repair Machines"],"id":["Repair Machines"]}},{"key":"beacon-2","label":{"en":"Repair Machine","id":"Repair Machine"},"definition":{"en":"One machine that produces one assigned repair material every eight seconds.","id":"Satu mesin yang menghasilkan satu jenis material perbaikan setiap delapan detik."},"aliases":{"en":["Repair Machine"],"id":["Repair Machine"]}},{"key":"beacon-3","label":{"en":"Output Tray","id":"Output Tray"},"definition":{"en":"The machine output that stores up to eight produced blocks.","id":"Tempat hasil mesin yang menyimpan maksimal delapan block."},"aliases":{"en":["Output Tray"],"id":["Output Tray"]}},{"key":"beacon-4","label":{"en":"Ghost Scaffold","id":"Ghost Scaffold"},"definition":{"en":"The guided structure with exactly 30 valid material positions.","id":"Struktur panduan dengan tepat 30 posisi material yang valid."},"aliases":{"en":["Ghost Scaffold"],"id":["Ghost Scaffold"]}},{"key":"beacon-5","label":{"en":"Main Beacon","id":"Main Beacon"},"definition":{"en":"The damaged summit structure rebuilt with repair material and powered by the Beacon Core.","id":"Struktur utama di summit yang dibangun kembali menggunakan material perbaikan dan ditenagai Beacon Core."},"aliases":{"en":["Main Beacon"],"id":["Main Beacon"]}},{"key":"beacon-6","label":{"en":"Shelter","id":"Shelter"},"definition":{"en":"The protected area that prevents Storm Exposure while the player remains inside.","id":"Area aman yang mencegah Storm Exposure selama player berada di dalamnya."},"aliases":{"en":["Shelter"],"id":["Shelter"]}},{"key":"beacon-7","label":{"en":"Storm Exposure","id":"Storm Exposure"},"definition":{"en":"One exposure recorded when a storm detects the player outside Shelter. Only one can be recorded per storm.","id":"Satu paparan yang dicatat saat badai mendeteksi player di luar Shelter. Maksimal satu paparan dicatat pada setiap badai."},"aliases":{"en":["Storm Exposure"],"id":["Storm Exposure"]}},{"key":"beacon-8","label":{"en":"Beacon Score","id":"Beacon Score"},"definition":{"en":"The Objective 3 score made from 80% Time Score and 20% Exposure Score.","id":"Nilai Objective 3 yang berasal dari 80% Time Score dan 20% Exposure Score."},"aliases":{"en":["Beacon Score"],"id":["Beacon Score"]}},{"key":"beacon-9","label":{"en":"Time Score","id":"Time Score"},"definition":{"en":"The score based on completion time. Nine minutes is standard; faster adds score and slower reduces score.","id":"Nilai berdasarkan waktu penyelesaian. Sembilan menit adalah standar; lebih cepat menambah nilai dan lebih lambat mengurangi nilai."},"aliases":{"en":["Time Score"],"id":["Time Score"]}},{"key":"beacon-10","label":{"en":"Exposure Score","id":"Exposure Score"},"definition":{"en":"The score based on Storm Exposure. It starts at 100 and loses 15 for each exposed storm.","id":"Nilai berdasarkan Storm Exposure. Nilai dimulai dari 100 dan berkurang 15 pada setiap badai yang mengenai player."},"aliases":{"en":["Exposure Score"],"id":["Exposure Score"]}}],"relay":[{"key":"relay-0","label":{"en":"Main Power Source","id":"Main Power Source"},"definition":{"en":"The origin point for all five Power Relay connections.","id":"Titik awal untuk seluruh lima sambungan Power Relay."},"aliases":{"en":["Main Power Source"],"id":["Main Power Source"]}},{"key":"relay-1","label":{"en":"Ghost Cable Paths","id":"Ghost Cable Paths"},"definition":{"en":"The five fixed placement routes connecting the Main Power Source to the Power Nodes.","id":"Lima jalur penempatan tetap yang menghubungkan Main Power Source dengan Power Nodes."},"aliases":{"en":["Ghost Cable Paths"],"id":["Ghost Cable Paths"]}},{"key":"relay-2","label":{"en":"Ghost Cable Path","id":"Ghost Cable Path"},"definition":{"en":"One fixed color route connecting the Main Power Source to one Power Node.","id":"Satu jalur warna tetap yang menghubungkan Main Power Source dengan satu Power Node."},"aliases":{"en":["Ghost Cable Path"],"id":["Ghost Cable Path"]}},{"key":"relay-3","label":{"en":"Power Nodes","id":"Power Nodes"},"definition":{"en":"The five city power connections that must be active at the same time.","id":"Lima sambungan tenaga kota yang harus aktif secara bersamaan."},"aliases":{"en":["Power Nodes"],"id":["Power Nodes"]}},{"key":"relay-4","label":{"en":"Power Node","id":"Power Node"},"definition":{"en":"One connection that activates only when every position in its Ghost Cable Path is correct.","id":"Satu sambungan yang aktif hanya ketika seluruh posisi pada Ghost Cable Path-nya benar."},"aliases":{"en":["Power Node"],"id":["Power Node"]}},{"key":"relay-5","label":{"en":"Storage Room","id":"Storage Room"},"definition":{"en":"The room containing eight chests with the full cable stock required for Power Relay.","id":"Ruangan berisi delapan chest dengan seluruh persediaan cable yang dibutuhkan untuk Power Relay."},"aliases":{"en":["Storage Room"],"id":["Storage Room"]}},{"key":"relay-6","label":{"en":"Shelter","id":"Shelter"},"definition":{"en":"A protected area that prevents exposure, debuffs, and carried-cable loss during a storm.","id":"Area aman yang mencegah paparan, efek negatif, dan kehilangan cable yang dibawa selama badai."},"aliases":{"en":["Shelter"],"id":["Shelter"]}},{"key":"relay-7","label":{"en":"Storm Cycle","id":"Storm Cycle"},"definition":{"en":"The repeating 75-second build period followed by a 15-second storm.","id":"Siklus berulang berupa 75 detik waktu membangun lalu 15 detik badai."},"aliases":{"en":["Storm Cycle"],"id":["Storm Cycle"]}},{"key":"relay-8","label":{"en":"Storm Exposure","id":"Storm Exposure"},"definition":{"en":"One exposure recorded when a storm detects the player outside Shelter. Only one can be recorded per storm.","id":"Satu paparan yang dicatat saat badai mendeteksi player di luar Shelter. Maksimal satu paparan dicatat pada setiap badai."},"aliases":{"en":["Storm Exposure"],"id":["Storm Exposure"]}},{"key":"relay-9","label":{"en":"Relay Score","id":"Relay Score"},"definition":{"en":"The Objective 4 score made from 80% Time Score and 20% Exposure Score.","id":"Nilai Objective 4 yang berasal dari 80% Time Score dan 20% Exposure Score."},"aliases":{"en":["Relay Score"],"id":["Relay Score"]}},{"key":"relay-10","label":{"en":"Time Score","id":"Time Score"},"definition":{"en":"The score based on completion time. Nine minutes is standard; faster adds score and slower reduces score.","id":"Nilai berdasarkan waktu penyelesaian. Sembilan menit adalah standar; lebih cepat menambah nilai dan lebih lambat mengurangi nilai."},"aliases":{"en":["Time Score"],"id":["Time Score"]}},{"key":"relay-11","label":{"en":"Exposure Score","id":"Exposure Score"},"definition":{"en":"The score based on Storm Exposure. It starts at 100, loses 15 per exposed storm, and never goes below 0.","id":"Nilai berdasarkan Storm Exposure. Nilai dimulai dari 100, berkurang 15 pada setiap badai yang mengenai player, dan tidak pernah kurang dari 0."},"aliases":{"en":["Exposure Score"],"id":["Exposure Score"]}}],"ending":[{"key":"ending-0","label":{"en":"Steampunk Hero Badge","id":"Steampunk Hero Badge"},"definition":{"en":"The final reward granted once after Emberhold is restored.","id":"Hadiah akhir yang diberikan satu kali setelah Emberhold berhasil dipulihkan."},"aliases":{"en":["Steampunk Hero Badge"],"id":["Steampunk Hero Badge"]}},{"key":"ending-1","label":{"en":"Final Total","id":"Final Total"},"definition":{"en":"The equal-weight average of Quarry Score, Ascent Score, Beacon Score, and Relay Score.","id":"Rata-rata dengan bobot sama dari Quarry Score, Ascent Score, Beacon Score, dan Relay Score."},"aliases":{"en":["Final Total"],"id":["Final Total"]}},{"key":"ending-2","label":{"en":"Objective Score","id":"Objective Score"},"definition":{"en":"One completed score from Quarry, Ascent, Beacon, or Relay.","id":"Satu score selesai yang berasal dari Quarry, Ascent, Beacon, atau Relay."},"aliases":{"en":["Objective Score"],"id":["Objective Score"]}},{"key":"ending-3","label":{"en":"Pending Recovery Record","id":"Pending Recovery Record"},"definition":{"en":"The backup record created when the main session result cannot be stored after all retries.","id":"Catatan cadangan yang dibuat saat hasil sesi utama tidak dapat disimpan setelah seluruh percobaan."},"aliases":{"en":["Pending Recovery Record"],"id":["Pending Recovery Record"]}},{"key":"ending-4","label":{"en":"Assigned Arena","id":"Assigned Arena"},"definition":{"en":"The isolated gameplay area used by the completed player or session and reset after lobby return.","id":"Area gameplay terpisah yang digunakan oleh player atau sesi yang selesai dan di-reset setelah kembali ke lobby."},"aliases":{"en":["Assigned Arena"],"id":["Assigned Arena"]}},{"key":"ending-5","label":{"en":"Session Result","id":"Session Result"},"definition":{"en":"The stored record containing the four Objective Scores, Final Total, reward state, and completion data.","id":"Data tersimpan yang berisi empat Objective Score, Final Total, status hadiah, dan data penyelesaian."},"aliases":{"en":["Session Result"],"id":["Session Result"]}},{"key":"ending-6","label":{"en":"Steampunk Communicator","id":"Steampunk Communicator"},"definition":{"en":"The protected communication item removed during final cleanup.","id":"Item komunikasi terlindungi yang dihapus saat pembersihan akhir."},"aliases":{"en":["Steampunk Communicator"],"id":["Steampunk Communicator"]}},{"key":"ending-7","label":{"en":"Beacon Core","id":"Beacon Core"},"definition":{"en":"The protected objective item removed from temporary gameplay state during final cleanup.","id":"Item objektif terlindungi yang dihapus dari kondisi gameplay sementara saat pembersihan akhir."},"aliases":{"en":["Beacon Core"],"id":["Beacon Core"]}}],"system":[{"key":"system-0","label":{"en":"Game System","id":"Game System"},"definition":{"en":"The main project-wide system that controls sessions, arena ownership, objectives, protected items, feedback, data, scoring, interruptions, and reset.","id":"Sistem utama project yang mengatur session, kepemilikan arena, objective, item terlindungi, feedback, data, scoring, interupsi, dan reset."},"aliases":{"en":["Game System"],"id":["Game System"]}},{"key":"system-1","label":{"en":"Multi Session","id":"Multi Session"},"definition":{"en":"The ability to run several player sessions at the same time while every player uses a separate arena copy and separate gameplay data.","id":"Kemampuan menjalankan beberapa session player pada waktu yang sama, sementara setiap player menggunakan salinan arena dan data gameplay yang terpisah."},"aliases":{"en":["Multi Session"],"id":["Multi Session"]}},{"key":"system-2","label":{"en":"Session","id":"Session"},"definition":{"en":"One complete AFTERSHOCK playthrough owned by one player, from start until completion or interruption.","id":"Satu rangkaian permainan AFTERSHOCK milik satu player, dari awal sampai selesai atau terputus."},"aliases":{"en":["Session"],"id":["Session"]}},{"key":"system-3","label":{"en":"Session ID","id":"Session ID"},"definition":{"en":"The unique identifier that connects a player, arena, objective state, items, timers, scores, and stored results.","id":"Identitas unik yang menghubungkan player, arena, kondisi objective, item, timer, score, dan hasil tersimpan."},"aliases":{"en":["Session ID"],"id":["Session ID"]}},{"key":"system-4","label":{"en":"Assigned Arena","id":"Assigned Arena"},"definition":{"en":"The separate arena copy reserved for one active Session and unavailable to other sessions until reset verification succeeds.","id":"Salinan arena terpisah yang digunakan oleh satu Session aktif dan tidak tersedia untuk session lain sampai pemeriksaan reset berhasil."},"aliases":{"en":["Assigned Arena"],"id":["Assigned Arena"]}},{"key":"system-5","label":{"en":"Session Data","id":"Session Data"},"definition":{"en":"The stored state for one session, including arena ownership, active objective, completed objectives, items, timers, progress, and scores.","id":"Data tersimpan untuk satu session, termasuk kepemilikan arena, objective aktif, objective selesai, item, timer, progress, dan score."},"aliases":{"en":["Session Data"],"id":["Session Data"]}},{"key":"system-6","label":{"en":"Session Ownership","id":"Session Ownership"},"definition":{"en":"The rule that links one player session to its arena and ensures all gameplay changes stay inside that session.","id":"Aturan yang menghubungkan satu session player dengan arenanya dan memastikan seluruh perubahan gameplay tetap berada pada session tersebut."},"aliases":{"en":["Session Ownership"],"id":["Session Ownership"]}},{"key":"system-7","label":{"en":"Gameplay Package","id":"Gameplay Package"},"definition":{"en":"One self-contained gameplay section with its own mechanic, setup, completion condition, data rules, scoring or completion data, and reset.","id":"Satu bagian gameplay mandiri dengan mechanic, setup, kondisi selesai, aturan data, scoring atau data penyelesaian, dan reset miliknya."},"aliases":{"en":["Gameplay Package","gameplay package"],"id":["Gameplay Package","gameplay package"]}},{"key":"system-8","label":{"en":"Objective Score","id":"Objective Score"},"definition":{"en":"One final score created only after Quarry, Ascent, Beacon, or Relay reaches its valid completion condition.","id":"Satu score akhir yang dibuat hanya setelah Quarry, Ascent, Beacon, atau Relay mencapai kondisi selesai yang valid."},"aliases":{"en":["Objective Score"],"id":["Objective Score"]}},{"key":"system-9","label":{"en":"Final Total","id":"Final Total"},"definition":{"en":"The final session value calculated from the four completed Objective Scores.","id":"Nilai akhir session yang dihitung dari empat Objective Score yang sudah selesai."},"aliases":{"en":["Final Total"],"id":["Final Total"]}},{"key":"system-10","label":{"en":"Session Result","id":"Session Result"},"definition":{"en":"The stored final record containing the Session ID, four Objective Scores, Final Total, completion state, reward state, and completion time.","id":"Data akhir tersimpan yang berisi Session ID, empat Objective Score, Final Total, status penyelesaian, status hadiah, dan waktu selesai."},"aliases":{"en":["Session Result"],"id":["Session Result"]}},{"key":"system-11","label":{"en":"Pending Recovery Record","id":"Pending Recovery Record"},"definition":{"en":"The backup record created when the main final save still fails after all retries.","id":"Catatan cadangan yang dibuat saat penyimpanan akhir utama tetap gagal setelah seluruh percobaan."},"aliases":{"en":["Pending Recovery Record"],"id":["Pending Recovery Record"]}}],"flow":[{"key":"flow-0","label":{"en":"Start Gate","id":"Start Gate"},"definition":{"en":"The lobby entrance that starts a new Session after an available arena has been assigned.","id":"Pintu masuk di lobby yang memulai Session baru setelah arena yang tersedia sudah ditetapkan."},"aliases":{"en":["Start Gate"],"id":["Start Gate"]}},{"key":"flow-1","label":{"en":"Multi Session","id":"Multi Session"},"definition":{"en":"The ability to let several players play at the same time while each player uses a separate Session, arena, and gameplay data.","id":"Kemampuan beberapa player bermain pada waktu yang sama, sementara setiap player menggunakan Session, arena, dan data gameplay yang terpisah."},"aliases":{"en":["Multi Session"],"id":["Multi Session"]}},{"key":"flow-2","label":{"en":"Session","id":"Session"},"definition":{"en":"One complete AFTERSHOCK journey owned by one player, from the Start Gate until completion or interruption.","id":"Satu perjalanan AFTERSHOCK lengkap milik satu player, dari Start Gate sampai selesai atau terputus."},"aliases":{"en":["Session"],"id":["Session"]}},{"key":"flow-3","label":{"en":"Assigned Arena","id":"Assigned Arena"},"definition":{"en":"The separate copy of Emberhold reserved for one active player Session.","id":"Salinan Emberhold terpisah yang digunakan khusus oleh satu Session player aktif."},"aliases":{"en":["Assigned Arena"],"id":["Assigned Arena"]}},{"key":"flow-4","label":{"en":"Emberhold","id":"Emberhold"},"definition":{"en":"The damaged floating-island city that the player restores throughout AFTERSHOCK.","id":"Kota pulau terapung yang rusak dan dipulihkan player sepanjang AFTERSHOCK."},"aliases":{"en":["Emberhold"],"id":["Emberhold"]}},{"key":"flow-5","label":{"en":"The Docks","id":"The Docks"},"definition":{"en":"The opening tutorial area where the player repairs the entrance route and receives Brann’s mission.","id":"Area tutorial pembuka tempat player memperbaiki jalur masuk dan menerima misi dari Brann."},"aliases":{"en":["The Docks"],"id":["The Docks"]}},{"key":"flow-6","label":{"en":"The Quarry","id":"The Quarry"},"definition":{"en":"Objective 1, where the player mines and processes material to create a new Beacon Core.","id":"Objective 1, tempat player menambang dan memproses material untuk membuat Beacon Core baru."},"aliases":{"en":["The Quarry"],"id":["The Quarry"]}},{"key":"flow-7","label":{"en":"The Ascent","id":"The Ascent"},"definition":{"en":"Objective 2, where the player carries the protected Beacon Core from The Quarry to the summit.","id":"Objective 2, tempat player membawa Beacon Core terlindungi dari The Quarry menuju summit."},"aliases":{"en":["The Ascent"],"id":["The Ascent"]}},{"key":"flow-8","label":{"en":"Beacon Core","id":"Beacon Core"},"definition":{"en":"The replacement power source created in The Quarry and carried to the Main Beacon.","id":"Sumber tenaga pengganti yang dibuat di The Quarry dan dibawa menuju Main Beacon."},"aliases":{"en":["Beacon Core"],"id":["Beacon Core"]}},{"key":"flow-9","label":{"en":"Main Beacon","id":"Main Beacon"},"definition":{"en":"The damaged summit structure that must be rebuilt before Emberhold can distribute power again.","id":"Struktur rusak di summit yang harus dibangun kembali sebelum Emberhold dapat menyalurkan tenaga lagi."},"aliases":{"en":["Main Beacon"],"id":["Main Beacon"]}},{"key":"flow-10","label":{"en":"Power Relay","id":"Power Relay"},"definition":{"en":"Objective 4, where five power routes are rebuilt so the Main Beacon can power the city.","id":"Objective 4, tempat lima jalur tenaga dibangun kembali agar Main Beacon dapat menyalakan kota."},"aliases":{"en":["Power Relay"],"id":["Power Relay"]}}]};
  const tooltip = document.getElementById('globalGlossaryTooltip');
  const tooltipTerm = document.getElementById('globalGlossaryTooltipTerm');
  const tooltipDefinition = document.getElementById('globalGlossaryTooltipDefinition');
  let activeTarget = null;
  let pinned = false;
  let hideTimer = null;

  const phaseFromSection = (section) => (section?.dataset.phase || '').replace(/^dev-/, '');
  const isWordChar = (character) => character ? /[\p{L}\p{N}_]/u.test(character) : false;

  function collectMatches(text, terms, language){
    const lower = text.toLocaleLowerCase(language === 'id' ? 'id' : 'en');
    const candidates = [];
    terms.forEach((term) => {
      const aliases = term.aliases[language] || term.aliases.en || [];
      aliases.forEach((alias) => {
        const needle = alias.toLocaleLowerCase(language === 'id' ? 'id' : 'en');
        let from = 0;
        while (needle && from < lower.length){
          const index = lower.indexOf(needle, from);
          if (index < 0) break;
          const before = index > 0 ? text[index - 1] : '';
          const after = index + alias.length < text.length ? text[index + alias.length] : '';
          if (!isWordChar(before) && !isWordChar(after)){
            candidates.push({start:index,end:index+alias.length,length:alias.length,term});
          }
          from = index + Math.max(1, needle.length);
        }
      });
    });
    candidates.sort((a,b) => a.start - b.start || b.length - a.length);
    const selected = [];
    let cursor = -1;
    for (const candidate of candidates){
      if (candidate.start >= cursor){
        selected.push(candidate);
        cursor = candidate.end;
      }
    }
    return selected;
  }

  function shouldSkip(node){
    return Boolean(node.closest(
      'script,style,#globalGlossaryTooltip,.sidebar,.page-head,.page-foot,.section-tabs,' +
      '.language-switch,.theme-switch,.view-switch,a,button'
    ));
  }

  function rebuildGlossaryTerms(){
    hideTooltip();
    const language = document.documentElement.lang === 'id' ? 'id' : 'en';
    document.querySelectorAll('section[data-phase^="dev-"]').forEach((section) => {
      const phase = phaseFromSection(section);
      const terms = glossary[phase];
      if (!terms) return;
      section.querySelectorAll('.i18n-text').forEach((node) => {
        if (shouldSkip(node)) return;
        const raw = language === 'id' ? node.dataset.id : node.dataset.en;
        if (typeof raw !== 'string') return;
        node.textContent = raw;
        const matches = collectMatches(raw, terms, language);
        if (!matches.length) return;
        const fragment = document.createDocumentFragment();
        let cursor = 0;
        matches.forEach((match) => {
          if (match.start > cursor) fragment.append(document.createTextNode(raw.slice(cursor, match.start)));
          const button = document.createElement('button');
          button.type = 'button';
          button.className = 'glossary-term';
          button.dataset.glossaryPhase = phase;
          button.dataset.glossaryKey = match.term.key;
          button.setAttribute('aria-expanded', 'false');
          button.setAttribute('aria-describedby', 'globalGlossaryTooltip');
          button.textContent = raw.slice(match.start, match.end);
          fragment.append(button);
          cursor = match.end;
        });
        if (cursor < raw.length) fragment.append(document.createTextNode(raw.slice(cursor)));
        node.replaceChildren(fragment);
      });
    });
  }

  function getTerm(target){
    const phase = target?.dataset.glossaryPhase;
    const key = target?.dataset.glossaryKey;
    return (glossary[phase] || []).find((term) => term.key === key) || null;
  }

  function positionTooltip(target){
    if (!target || !tooltip.classList.contains('is-visible')) return;
    const rect = target.getBoundingClientRect();
    const mobile = window.matchMedia('(max-width:720px)').matches;
    if (mobile) return;
    const margin = 12;
    const gap = 12;
    const tipRect = tooltip.getBoundingClientRect();
    const placeTop = rect.top >= tipRect.height + gap + margin;
    const placement = placeTop ? 'top' : 'bottom';
    let top = placeTop ? rect.top - tipRect.height - gap : rect.bottom + gap;
    top = Math.max(margin, Math.min(top, window.innerHeight - tipRect.height - margin));
    let left = rect.left + rect.width / 2 - tipRect.width / 2;
    left = Math.max(margin, Math.min(left, window.innerWidth - tipRect.width - margin));
    const arrowLeft = Math.max(14, Math.min(rect.left + rect.width / 2 - left, tipRect.width - 14));
    tooltip.dataset.placement = placement;
    tooltip.style.top = `${Math.round(top)}px`;
    tooltip.style.left = `${Math.round(left)}px`;
    tooltip.style.setProperty('--arrow-left', `${Math.round(arrowLeft)}px`);
  }

  function showTooltip(target, shouldPin=false){
    const term = getTerm(target);
    if (!term) return;
    clearTimeout(hideTimer);
    if (activeTarget && activeTarget !== target) activeTarget.setAttribute('aria-expanded', 'false');
    activeTarget = target;
    pinned = shouldPin;
    const language = document.documentElement.lang === 'id' ? 'id' : 'en';
    tooltipTerm.textContent = term.label[language] || term.label.en;
    tooltipDefinition.textContent = term.definition[language] || term.definition.en;
    tooltip.classList.add('is-visible');
    tooltip.setAttribute('aria-hidden', 'false');
    target.setAttribute('aria-expanded', 'true');
    requestAnimationFrame(() => positionTooltip(target));
  }

  function hideTooltip(force=true){
    clearTimeout(hideTimer);
    if (!force && pinned) return;
    if (activeTarget) activeTarget.setAttribute('aria-expanded', 'false');
    activeTarget = null;
    pinned = false;
    tooltip.classList.remove('is-visible');
    tooltip.setAttribute('aria-hidden', 'true');
  }

  document.addEventListener('pointerover', (event) => {
    const target = event.target.closest?.('.glossary-term');
    if (!target || event.pointerType === 'touch' || pinned) return;
    showTooltip(target, false);
  });
  document.addEventListener('pointerout', (event) => {
    const target = event.target.closest?.('.glossary-term');
    if (!target || pinned) return;
    hideTimer = setTimeout(() => hideTooltip(false), 90);
  });
  document.addEventListener('focusin', (event) => {
    const target = event.target.closest?.('.glossary-term');
    if (target) showTooltip(target, false);
  });
  document.addEventListener('focusout', (event) => {
    if (event.target.closest?.('.glossary-term') && !pinned) hideTooltip(true);
  });
  document.addEventListener('click', (event) => {
    const target = event.target.closest?.('.glossary-term');
    if (target){
      event.preventDefault();
      event.stopPropagation();
      if (activeTarget === target && pinned) hideTooltip(true);
      else showTooltip(target, true);
      return;
    }
    hideTooltip(true);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') hideTooltip(true);
    if ((event.key === 'Enter' || event.key === ' ') && event.target.closest?.('.glossary-term')){
      event.preventDefault();
      event.target.click();
    }
  });
  window.addEventListener('scroll', () => {
    if (activeTarget && pinned) positionTooltip(activeTarget);
    else hideTooltip(true);
  }, {passive:true});
  window.addEventListener('resize', () => activeTarget ? positionTooltip(activeTarget) : null);
  window.addEventListener('hashchange', () => hideTooltip(true));

  const observer = new MutationObserver((mutations) => {
    if (mutations.some((mutation) => mutation.type === 'attributes' && mutation.attributeName === 'lang')){
      queueMicrotask(rebuildGlossaryTerms);
    }
  });
  observer.observe(document.documentElement, {attributes:true, attributeFilter:['lang']});

  window.rebuildGlossaryTerms = rebuildGlossaryTerms;
  rebuildGlossaryTerms();
})();
