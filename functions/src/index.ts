import * as functions from "firebase-functions";

// // Start writing functions
// // https://firebase.google.com/docs/functions/typescript
//
// export const helloWorld = functions.https.onRequest((request, response) => {
//   functions.logger.info("Hello logs!", {structuredData: true});
//   response.send("Hello from Firebase!");
// });
import express = require("express");
import cors = require("cors");

// Create App
const app = express();

// Automatically allow cross-origin requests
app.use(cors({ origin: true }));

// Add middleware to authenticate requests
//app.use(myMiddleware);

// build multiple CRUD interfaces:
app.get('/', (req, res) => res.send(
    {"status_code":200, "message":"Works as"}
));


// Expose Express API as a single Cloud Function:
exports.free_hosting = functions.https.onRequest(app);