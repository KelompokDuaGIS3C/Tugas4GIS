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