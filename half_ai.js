// Part 1 - Looks AI generated
// --------------------------------------------
// This section handles setting up a simple Express server
// It defines endpoints for greeting users
// NOTE: This is an example and may not be production-ready

const express = require("express");
const app = express();
app.use(express.json());

/**
 * GET /hello
 * Returns a greeting message with the provided name
 */
app.get("/hello/:name", (req, res) => {
  const { name } = req.params;
  res.json({ message: `Hello, ${name}!` });
});

// --------------------------------------------
// Part 2 - Looks more human (messy style)
// --------------------------------------------

// TODO: clean this up later
let counter=0

// dumb endpoint just to test, idc if it crashes lol
app.get("/count",(req,res)=>{
counter++
res.send("count="+counter) // not using json, too lazy
})

// quick hack: reset counter (should prob be secured)
app.post("/reset",function(r,s){
counter=0
s.send("ok")
})


// Start the server
app.listen(3000, ()=>console.log("server on 3000"))
