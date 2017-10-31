import folium 

m = folium.Map(
location=[3.597031, 98.678513],
zoom_start=12,
tiles='Stamen Terrain')

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


m
# huruf m diatas jangan di hapus! by adam!