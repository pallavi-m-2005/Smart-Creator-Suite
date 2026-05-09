import psutil
import matplotlib.pyplot as plt


def get_system_stats():
    return {
        "CPU": psutil.cpu_percent(),
        "RAM": psutil.virtual_memory().percent,
        "Disk": psutil.disk_usage('/').percent
    }


def plot_graph(data, title):

    fig, ax = plt.subplots()

    ax.plot(data)

    ax.set_title(title)

    ax.set_xlabel("Time")

    ax.set_ylabel("Usage %")

    return fig
