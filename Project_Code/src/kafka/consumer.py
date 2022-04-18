def consumer_fun():

    # import pip
    # from kafka.producer import kafka

    # pip install kafka-python
    from kafka import KafkaConsumer

    # Consuming the domains from kafka

    consumer = KafkaConsumer(
        'ml-raw-dns',
        bootstrap_servers = ['localhost:9092'],
        auto_offset_reset = 'earliest',
        enable_auto_commit = False
    )

    count = 100000
    retrieved_messages = []
    for i in consumer:
        print(i.value.decode("utf8"))
        retrieved_messages.append(i.value.decode("utf8"))
        count -= 1
        if(count == 0):
            break

    print(len(retrieved_messages))

    import pandas as pd
    df = pd.DataFrame (retrieved_messages, columns = ['domain'])

    print(df.head())
    # df.to_csv("D:/Local Disk D/DEBI/UOttawa/Term 2/AI For Cyber Security/Assignment/Individual/2/Part 2/all_domain_data/all_domains_dataset.csv", index=False)
    df.to_csv("../data/all_domains_dataset.csv", index=False)

consumer_fun()

