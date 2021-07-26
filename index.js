router.get("/",(req,res)=>{
    res.send({response:"how are you"}).status(200);
});

module.exports=router;