import hazelcast
import time

def consume():
    # Create a Hazelcast client and connect to the cluster
    client = hazelcast.HazelcastClient(cluster_members=["183.158.69.103:4704", "183.158.69.103:4705", "183.158.69.103:4706"])
    
    try:
        # Get the distributed queue named "bounded-queue"
        queue = client.get_queue("bounded-queue").blocking()
        
        # Continuously consume items from the queue
        while True:
            item = queue.take()
            print(f"Consumed: {item}")
            
    finally:
        # Shutdown the Hazelcast client to release resources
        client.shutdown()

if __name__ == "__main__":
    consume()
