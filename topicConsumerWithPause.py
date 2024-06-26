import hazelcast
import time

def task4_2():
    # Create a Hazelcast client and connect to the cluster
    client = hazelcast.HazelcastClient(cluster_members=["183.158.69.103:4704", "183.158.69.103:4705", "183.158.69.103:4706"])
    
    try:
        # Get the distributed topic named "my-distributed-topic"
        topic = client.get_topic("my-distributed-topic")
        
        # Define a listener function to handle incoming messages
        listener = topic.add_listener(lambda message: print(f"Received: {message.message}"))
        
        # Pause execution for 10 seconds to listen for messages
        time.sleep(10)
        
        # Wait for user input to stop the listener (typically press Enter)
        input("Press Enter to stop...\n")
        
    finally:
        # Shutdown the Hazelcast client
        client.shutdown()

if __name__ == "__main__":
    task4_2()
