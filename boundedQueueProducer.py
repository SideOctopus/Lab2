import hazelcast
import time

def produce():
    # Create a Hazelcast client and connect to the cluster
    client = hazelcast.HazelcastClient(cluster_members=["183.158.69.103:4704", "183.158.69.103:4705", "183.158.69.103:4706"])
    
    try:
        # Get the distributed queue named "bounded-queue"
        queue = client.get_queue("bounded-queue").blocking()
        
        # Produce items (numbers 1 to 100) and enqueue them
        for i in range(1, 101):
            queue.put(i)
            print(f"Produced: {i}")
            time.sleep(0.1)  # Introducing a small delay for demonstration
            
    finally:
        # Shutdown the Hazelcast client to release resources
        client.shutdown()

if __name__ == "__main__":
    produce()
