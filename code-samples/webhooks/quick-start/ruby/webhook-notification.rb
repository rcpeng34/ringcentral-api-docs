require 'ringcentral'
require 'dotenv/load'

DELIVERY_ADDRESS = '<https://xxxxxxxx.ngrok.io>'

$rc = RingCentral.new( ENV['RC_CLIENT_ID'],
                       ENV['RC_CLIENRT_SECRET'],
                       ENV['RC_SERVER_URL'] )

$rc.authorize( username: ENV['RC_USERNAME'],
               extension: ENV['RC_EXTENSION'],
               password: ENV['RC_PASSWORD'] )

r = $rc.post('/restapi/v1.0/subscription', payload: {
    eventFilters: ['/restapi/v1.0/account/~/extension/~/message-store/instant?type=SMS'],
    deliveryMode: { transportType: 'WebHook', address: DELIVERY_ADDRESS }
})

puts r.body['id']
puts "WebHook Ready"

$rc.revoke()
