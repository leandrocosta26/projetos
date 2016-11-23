import pika
import threading
import sys
import pdb

def write_queue(x):
  # pdb.set_trace()
  print(x)
  connection = pika.BlockingConnection(pika.ConnectionParameters(
          host='localhost'))
  channel = connection.channel()
  
  channel.exchange_declare(exchange='spartacus-providers-evaluations-request-exchange',
                           type='topic', durable=True)
  
  routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
  message = '{"orderId":"' + str(x) + '","reanalysis":false,"providerName":"CLEAR_SALE","isPerformance":false}'
  channel.basic_publish(exchange='spartacus-providers-evaluations-request-exchange',
                        routing_key="CLEAR_SALE",
                        body=message,
                        properties=pika.BasicProperties(
                            delivery_mode = 2
                           ,content_encoding='UTF-8'
                           ,content_type='application/json'
                           ,headers = {'__TypeId__': 'spartacus.sharedvos.v1.queues.spartacus.providers.QMV1SpartacusProviderEvaluationRequest',
                                     'x-tid':    'SPAR-dsz80zn7k0ov0hv8wh57no5pl'}
                        ))
  
  print(" [x] Sent %r:%r" % (routing_key, message))
  connection.close()

def main(argv):
    for x in range(1,300000):
      t = threading.Thread(write_queue(x))
      t.daemon = True
      t.start()
        

if __name__ == "__main__":
    main(sys.argv)    