import folium 

def peta(long,lat):
	m = folium.Map(
    location=[long,lat],
    zoom_start=12,
    tiles='Stamen Terrain')
	return m
	
def coba(long,lat):
	p = folium.Map(
    location=[long,lat],
    zoom_start=12,
    tiles='Stamen Terrain')	
	return p

def pungsi(long,lat):
	d = folium.Map(
	location=[long,lat],
	zoom_start=12,
    tiles='Stamen Terrain')	
	return d
	
def save(pusing, kepala):
	pusing.save(kepala)

m = peta(3.597031, 98.678513)
p = coba(3.597031, 98.678513)
d = pungsi(3.597031, 98.678513)
tooltip = 'Click me!'

folium.Marker([3.590678, 98.678527], popup='<i>Lapangan Merdeka</i>').add_to(m)
folium.Marker([3.590705, 98.677671], popup='<i>Amanda</i>').add_to(m)
folium.Marker([3.590459, 98.677830], popup='<i>Batiks Urban Cafe</i>').add_to(m)
folium.Marker([3.590344, 98.677846], popup='<i>Warung Kopi Srikandi</i>').add_to(m)
folium.Marker([3.590381, 98.679345], popup='<i>Pasar Buku Medan</i>').add_to(m)
folium.Marker([3.590828, 98.677570], popup='<i>Kaha</i>').add_to(m)
folium.Marker([3.591136, 98.677543], popup='<i>Teri Bajar Medan</i>').add_to(m)
folium.Marker([3.590983, 98.677537], popup='<i>Badjoe Kinantan</i>').add_to(m)
folium.Marker([3.591601, 98.678141], popup='<i>Rumah Makan Bukit Barisan</i>').add_to(m)
folium.Marker([3.590613, 98.680524], popup='<i>Kantor Polsek Medan Timur</i>').add_to(m)

folium.Marker([3.688517, 98.661182], popup='<i>Toko Kita</i>').add_to(m)
folium.Marker([3.688632, 98.660871], popup='<i>Optik Sucou</i>').add_to(m)
folium.Marker([3.688533, 98.660654], popup='<i>Cafe Wulan</i>').add_to(m)
folium.Marker([3.688346, 98.660970], popup='<i>Warung Nasgor Uwo</i>').add_to(m)
folium.Marker([3.688370, 98.660487], popup='<i>Pangkas ATM</i>').add_to(m)
folium.Marker([3.688161, 98.661126], popup='<i>Warung BU JUS</i>').add_to(m)
folium.Marker([3.688865, 98.660769], popup='<i>Kampus LP3I</i>').add_to(m)
folium.Marker([3.688924, 98.660048], popup='<i>Mitra Jaya Perabot</i>').add_to(m)
folium.Marker([3.688985, 98.659887], popup='<i>Warung Sticker</i>').add_to(m)
folium.Marker([3.689044, 98.660338], popup='<i>Wihara Maitreya Loka</i>').add_to(m)

folium.Marker([3.529454, 98.743142], popup='<i>Komplek Taman Riviera</i>').add_to(m)
folium.Marker([3.530242, 98.742922], popup='<i>Atlas Copco Indonesia. PT - Taman Riviera</i>').add_to(m)
folium.Marker([3.531529, 98.744600], popup='<i>Mbak Inah Riviera</i>').add_to(m)
folium.Marker([3.531370, 98.744229], popup='<i>Warung Langkah Baru</i>').add_to(m)
folium.Marker([3.531892, 98.744995], popup='<i>Tugu Batas Kota</i>').add_to(m)
folium.Marker([3.532369, 98.742211], popup='<i>Traktor Nusantara. PT - Tanjung Morawa</i>').add_to(m)
folium.Marker([3.533399, 98.742658], popup='<i>Tamora Indah</i>').add_to(m)
folium.Marker([3.533520, 98.741224], popup='<i>Indomart Bangun Mulia</i>').add_to(m)
folium.Marker([3.534073, 98.740678], popup='<i>Kedai Kopi Tebol</i>').add_to(m)
folium.Marker([3.534414, 98.743773], popup='<i>Mora Indah</i>').add_to(m)

folium.Marker([3.618215, 98.678526], popup='<i>Sd Muhammadiyah 02</i>').add_to(m)
folium.Marker([3.618328, 98.678537], popup='<i>Smp Muhammadiyah 57</i>').add_to(m)
folium.Marker([3.590459, 98.677830], popup='<i>Batiks Urban Cafe</i>').add_to(m)
folium.Marker([3.618340, 98.678300], popup='<i>Rumah Sakit Widya Husada</i>').add_to(m)
folium.Marker([3.617989, 98.678204], popup='<i>Rumah Sakit Ibu & anak Az-Zakiyah </i>').add_to(m)
folium.Marker([3.618450, 98.677978], popup='<i>Kak Inong</i>').add_to(m)
folium.Marker([3.617781, 98.677890], popup='<i>Pimpinan cabang Muhammadiyah</i>').add_to(m)
folium.Marker([3.617684, 98.678048], popup='<i>Mie balap kq5</i>').add_to(m)
folium.Marker([3.617342, 98.678282], popup='<i>Nazwa aneka kue</i>').add_to(m)
folium.Marker([3.617329, 98.678105], popup='<i>Nasi Goreng Teguh Jaya</i>').add_to(m)

folium.Marker([3.490658, 98.642756], popup='<i>CV.WELINDO SAONG UTAMA</i>').add_to(m)
folium.Marker([3.490983, 98.643065], popup='<i>Warung Muslim</i>').add_to(m)
folium.Marker([3.510058, 98.649614], popup='<i>Agung Ponsel</i>').add_to(m)
folium.Marker([3.510685, 98.649176], popup='<i>Gereja Methodist Indonesia</i>').add_to(m)
folium.Marker([3.510687, 98.649841], popup='<i>Alfamart Simalingkar B</i>').add_to(m)
folium.Marker([3.510838, 98.649783], popup='<i>RM BAKMI HENDRA</i>').add_to(m)
folium.Marker([3.511002, 98.649809], popup='<i>UD. Silaban</i>').add_to(m)
folium.Marker([3.511098, 98.650037], popup='<i>Dana Water</i>').add_to(m)
folium.Marker([3.511138, 98.649867], popup='<i>MIKHAEL PONSEL & KEDAI SARAPAN MIKHAEL S.</i>').add_to(m)
folium.Marker([3.511230, 98.649863], popup='<i>AM TOUR & TRAVEL</i>').add_to(m)

folium.Marker([3.617399, 98.678051], popup='<i>Habib ponsel</i>').add_to(m)
folium.Marker([3.617498, 98.678126], popup='<i>Rumah Makan Family Setia</i>').add_to(m)
folium.Marker([3.617756, 98.678195], popup='<i>tm Warkop</i>').add_to(m)
folium.Marker([3.618071, 98.679613], popup='<i>Strawberry Baby Shops</i>').add_to(m)
folium.Marker([3.618939, 98.678211], popup='<i>Brownies 4 Angel</i>').add_to(m)
folium.Marker([3.618978, 98.678116], popup='<i>Siomay Jakarta Mustafa</i>').add_to(m)
folium.Marker([3.619093, 98.678033], popup='<i>Drum Kupi</i>').add_to(m)
folium.Marker([3.688924, 98.660048], popup='<i>Mitra Jaya Perabot</i>').add_to(m)
folium.Marker([3.619246, 98.678666], popup='<i>Singkong Thailand Lumer Medan</i>').add_to(m)
folium.Marker([3.619381, 98.678235], popup='<i>Apotek Rezeki Tiga S</i>').add_to(m)

folium.Marker([3.6060894,98.6769312], popup='<i>Toko Bintang</i>').add_to(m)
folium.Marker([3.6058833,98.6767361], popup='<i>solid</i>').add_to(m)
folium.Marker([3.6058833,98.6767361], popup='<i>bintang 99</i>').add_to(m)
folium.Marker([3.6059863,98.6767602], popup='<i>restoran gaharu</i>').add_to(m)
folium.Marker([3.6063375,98.6765338], popup='<i>S.Sipayung Ponsel</i>').add_to(m)
folium.Marker([3.6066266,98.6770923], popup='<i>Pondok Kampoeng Bamboe Ayam Rica Rica</i>').add_to(m)
folium.Marker([3.6069385,98.6771058], popup='<i>Ikan Bakar Sibolga</i>').add_to(m)
folium.Marker([3.607603,98.6769737], popup='<i>Roy Mobil</i>').add_to(m)
folium.Marker([3.6071828,98.6763212], popup='<i>Radana Finance Medan</i>').add_to(m)
folium.Marker([3.6071225,98.6754636], popup='<i>Jasa Raharja</i>').add_to(m)

folium.Marker([3.619250, 98.677948], popup='<i>Ayam Penyet Sehat</i>').add_to(m)
folium.Marker([3.619641, 98.678353], popup='<i>Katty Kafee</i>').add_to(m)
folium.Marker([3.619703, 98.677999], popup='<i>Badan Nasional Penempatan dan Perlindungan Tenaga Kerja Indonesia</i>').add_to(m)
folium.Marker([3.619830, 98.678226], popup='<i>Sanggar Senam Widuri</i>').add_to(m)
folium.Marker([3.619608, 98.678060], popup='<i>Planet Of The Vapes / POTV express</i>').add_to(m)
folium.Marker([3.619651, 98.678279], popup='<i>Kalibre Store</i>').add_to(m)
folium.Marker([3.620511, 98.677904], popup='<i>PT. Total Data Persada</i>').add_to(m)
folium.Marker([3.620406, 98.678063], popup='<i>Gudang Bulog Mustafa</i>').add_to(m)
folium.Marker([3.620422, 98.678251], popup='<i>Koprasi Simpan Pinjam Cinta Kasih</i>').add_to(m)
folium.Marker([3.620710, 98.678343], popup='<i>Mega Multi. PT</i>').add_to(m)

folium.Marker([3.620923, 98.678272], popup='<i>D"LIMA WATER</i>').add_to(m)
folium.Marker([3.620534, 98.680605], popup='<i>IT Comm ( Authorized Service Center )</i>').add_to(m)
folium.Marker([3.620751, 98.680694], popup='<i>Angliss Bakehouse</i>').add_to(m)
folium.Marker([3.620303, 98.680704], popup='<i>Kedai Kopi Uleekareng & Gayo Krakatau</i>').add_to(m)
folium.Marker([3.620233, 98.680977], popup='<i>King Master Furniture</i>').add_to(m)
folium.Marker([3.620790, 98.681055], popup='<i>Longer Resto Cafe</i>').add_to(m)
folium.Marker([3.620706, 98.680510], popup='<i>auto88 mobil</i>').add_to(m)
folium.Marker([3.620056, 98.680708], popup='<i>TOP CUT Barbershop</i>').add_to(m)
folium.Marker([3.619950, 98.680754], popup='<i>Rumah Makan Pagi Sore</i>').add_to(m)
folium.Marker([3.620190, 98.680454], popup='<iArsitek Medan , MAT architect , MAT design schoo</i>').add_to(m)

folium.Marker([2.9652374,99.0559392], popup='<i>Taman Hewan Pematang Siantar</i>').add_to(m)
folium.Marker([2.9638971,99.0013521], popup='<i>GKPS Tengkoh</i>').add_to(m)
folium.Marker([2.9212955,98.9310997], popup='<i>Minolata Motor</i>').add_to(m)
folium.Marker([2.9462395,98.8881414], popup='<i>HKBP Merek Raya</i>').add_to(m)
folium.Marker([2.9550254,98.865525], popup='<i>SMA Plus PMS Raya</i>').add_to(m)
folium.Marker([2.9571255,98.8468569], popup='<i>SMK Negeri 1 raya</i>').add_to(m)
folium.Marker([2.9612827,98.826515], popup='<i>Kantor DPRDSiaungun</i>').add_to(m)
folium.Marker([2.9591398,98.7860458], popup='<i>GKPS Bandar Bayu</i>').add_to(m)
folium.Marker([2.9272101,98.7194412], popup='<i>KantorposTigarunggu</i>').add_to(m)
folium.Marker([2.9089626,98.679648], popup='<i>Rumah Bolon Raja Purba</i>').add_to(m)

folium.Marker([3.574007, 98.665819], popup='<i>Jimbaran Resto - Medan</i>').add_to(m)
folium.Marker([3.574059, 98.665408], popup='<i>Shoot. Pool Lounge & Sport Bar</i>').add_to(m)
folium.Marker([3.574329, 98.665296], popup='<i>The Traders Restaurant</i>').add_to(m)
folium.Marker([3.574377, 98.665695], popup='<i>Pocillo Coffee</i>').add_to(m)
folium.Marker([3.574595, 98.665442], popup='<i>All Day Bread & Pocillo Coffee</i>').add_to(m)
folium.Marker([3.574847, 98.665560], popup='<i>Bebek Ubud</i>').add_to(m)
folium.Marker([3.574424, 98.666487], popup='<i>Graha Siga. PT</i>').add_to(m)
folium.Marker([3.575052, 98.665787], popup='<i>Restoran Sederhana</i>').add_to(m)
folium.Marker([3.575090, 98.665578], popup='<i>WARUNG OMonde</i>').add_to(m)
folium.Marker([3.575227, 98.665636], popup='<i>Warung Nasi Selera Kita</i>').add_to(m)

folium.Marker([3.6514101,98.5873849], popup='<i>Polsek Medan Barat</i>').add_to(m)
folium.Marker([3.6768498,98.4794896], popup='<i>Polsek Medan Belawan</i>').add_to(m)
folium.Marker([3.6004877,98.6931626], popup='<i>Waroeng Wali Kuliner & Kopi</i>').add_to(m)
folium.Marker([3.6083462,98.4866872], popup='<i>Kuliner Q3</i>').add_to(m)
folium.Marker([3.6004877,98.6931626], popup='<i>Denai Kuliner</i>').add_to(m)
folium.Marker([3.5915316,98.7016375], popup='<i>SMP Negeri 12</i>').add_to(m)
folium.Marker([3.5915308,98.6776482], popup='<i>Universitas Islam Sumatera Utara Fakultas Kedokteran</i>').add_to(m)
folium.Marker([3.595201,98.6813256], popup='<i>UIN Sumatera Utara Pacsasarjana</i>').add_to(m)
folium.Marker([3.595201,98.6813256], popup='<i>SMA Negeri 3 Medan</i>').add_to(m)
folium.Marker([3.5948895,98.67719], popup='<i>Universitas Katolik Santo Thomas</i>').add_to(m)

m

folium.Circle( radius=100, location=[3.637861, 98.669650], popup='Momkids CV').add_to(p)
folium.Circle( radius=100, location=[3.638444, 98.669814], popup='Kos Yosafat').add_to(p)
folium.Circle( radius=100, location=[3.638655, 98.670361], popup='Lis Ponsel').add_to(p)
folium.Circle( radius=100, location=[3.638548, 98.669823], popup='DESRY ELEKTRIK').add_to(p)
folium.Circle( radius=100, location=[3.638720, 98.669437], popup='Angga Ponsel 2').add_to(p)
folium.Circle( radius=100, location=[3.638826, 98.669386], popup='Bu Neng Collection').add_to(p)
folium.Circle( radius=100, location=[3.638966, 98.669383], popup='Mirel Baby & Kids').add_to(p)
folium.Circle( radius=100, location=[3.639800, 98.669011], popup='Mukhsin hts tailor').add_to(p)
folium.Circle( radius=100, location=[3.640030, 98.668539], popup='Halim Ponsel').add_to(p)
folium.Circle( radius=100, location=[3.640894, 98.668319], popup='Vz Motor').add_to(p)

p

folium.Marker( location=[3.540923, 98.653942], popup='Warkop AADS').add_to(d)
folium.Marker( location=[3.540852, 98.654248], popup='Coffee Store Warkop Putri').add_to(d)
folium.Marker( location=[3.541015, 98.654292], popup='Adira Finance').add_to(d)
folium.Marker( location=[3.541177, 98.654298], popup='Bank BRI').add_to(d)
folium.Marker( location=[3.541055, 98.654162], popup='HD CAFE').add_to(d)
folium.Marker( location=[3.541178, 98.654056], popup='Permata Water').add_to(d)
folium.Marker( location=[3.541151, 98.654460], popup='UD.BIMA').add_to(d)
folium.Marker( location=[3.541389, 98.654427], popup='Auto Clean Service').add_to(d)
folium.Marker( location=[3.541334, 98.654582], popup='Toko Sepeda Pandiangan').add_to(d)
folium.Marker( location=[3.541495, 98.654794], popup='Bak mie Sp.pos').add_to(d)

d

save(m,'1.html')
save(p,'2.html')
save(d,'3.html')

# huruf m,p,d diatas jangan di hapus! by adam!
