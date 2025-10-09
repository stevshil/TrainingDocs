const { MongoClient } = require('mongodb');
const tls = require('tls');
const fs = require('fs')

const username = encodeURIComponent('root');
const password = encodeURIComponent('secret123');

const uri = 'mongodb://'+username+':'+password+'@127.0.0.1/example?authSource=admin';
console.log(uri);
// Unsecure
const client = new MongoClient(uri);
// console.log(client);

// Secure
// const uri = 'mongodb+srv://'+username+':'+password+'@127.0.0.1/example';
// const secureContext = tls.createSecureContext({
//     ca: fs.readFileSync('../certs/localhost.pem'),
//     cert: fs.readFileSync('../certs/localhost.cert'),
//     key: fs.readFileSync('../certs/localhost.key'),
//   });
// const client = new MongoClient(uri, { tls: true, secureContext });

async function run() {
    try {
        await client.connect();
        console.log('Connected to MongoDB successfully!');

        // Perform database operations here...
        const mydb=client.db("example");
        console.log("Connected to "+mydb.databaseName);
        const listings=await mydb.collection("listings");
        console.log("Connected to collection "+listings.collectionName);
        const query={ property_type: "House" };
        const listing=await listings.findOne(query);
        console.log("Found "+ listing)
        // console.log(listing);

    } catch (error) {
        console.error('Error connecting to MongoDB:', error);
    } finally {
        client.close();
    }
}

run().catch(console.dir); 