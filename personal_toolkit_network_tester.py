import speedtest

def run_speed_test():
    """
    Runs a network speed test and returns download and upload speeds in Mbps.
    """
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000    # Convert to Mbps
    return {"download_speed": download_speed, "upload_speed": upload_speed}