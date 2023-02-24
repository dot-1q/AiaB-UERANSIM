import speedtest

st = speedtest.Speedtest()
st.get_best_server()

download_speed = st.download() / 1_000_000
upload_speed = st.upload() / 1_000_000

print(f"Download speed: {download_speed} Mbps")
print(f"Upload speed: {upload_speed} Mbps")
