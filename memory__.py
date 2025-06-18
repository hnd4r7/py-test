import resource
import time
import signal
import sys

# Set memory limit to 500 MB (in bytes)
MEMORY_LIMIT = 50 * 1024 * 1024  # 50 MB


def signal_handler(sig, frame):
    """Print memory usage on termination."""
    usage = resource.getrusage(resource.RUSAGE_SELF)
    print(f"Memory usage before termination: {usage.ru_maxrss / 1024:.2f} MB")
    sys.exit(0)


# Register signal handlers for clean exit
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


def set_memory_limit():
    """Set the memory limit for the process."""
    try:
        # RLIMIT_AS limits the total virtual memory (address space)
        resource.setrlimit(resource.RLIMIT_AS, (MEMORY_LIMIT, MEMORY_LIMIT))
        print(f"Memory limit set to {MEMORY_LIMIT / 1024**2:.2f} MB")
    except ValueError as e:
        print(f"Failed to set memory limit: {e}")
        sys.exit(1)


def consume_memory():
    """Simulate memory consumption."""
    data = []
    while True:
        data.append(" " * 10_000_000)  # Allocate ~10MB per iteration
        usage = resource.getrusage(resource.RUSAGE_SELF)
        print(f"Current memory (RSS): {usage.ru_maxrss / 1024:.2f} MB")
        time.sleep(1)


if __name__ == "__main__":
    set_memory_limit()
    consume_memory()
