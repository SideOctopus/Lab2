import hazelcast

def main():
    # Create a Hazelcast client and connect to the cluster
    client = hazelcast.HazelcastClient(cluster_members=["183.158.69.103:4704", "183.158.69.103:4705", "183.158.69.103:4706"])
    
    # Get a distributed map named "capitals"
    distributed_map = client.get_map("capitals").blocking()

    # Insert 1000 key-value pairs into the map
    for i in range(1000):
        distributed_map.put(i, f"City {i}")

    # Print the size of the map
    print(f"Map size: {distributed_map.size()}")
    
    # Shutdown the Hazelcast client
    client.shutdown()

if __name__ == "__main__":
    main()