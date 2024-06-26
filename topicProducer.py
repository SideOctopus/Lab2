import hazelcast
import time

def task4_1():
    # Create a Hazelcast client and connect to the cluster
    client = hazelcast.HazelcastClient(cluster_members=["183.158.69.103:4704", "183.158.69.103:4705", "183.158.69.103:4706"])
    
    try:
        # Get a distributed topic named "my-distributed-topic"
        topic = client.get_topic("my-distributed-topic")
        
        # Publish numbers 1 to 100 to the topic
        for i in range(1, 101):
            topic.publish(i)
            print(f"Sent: {i}")
            time.sleep(0.1)  # Sleep to simulate delay between publishes
            
    finally:
        # Shutdown the Hazelcast client
        client.shutdown()

if __name__ == "__main__":
    task4_1()
