(function($){

    var Renderer = function(canvas){
        var canvas = $(canvas).get(0)
        var ctx = canvas.getContext("2d");
        var particleSystem
        ctx.font="10px Georgia";
        ctx.fillStyle = 'LavenderBlush';
        nodes_ready=true

        var that = {
            init:function(system){
                //
                // the particle system will call the init function once, right before the
                // first frame is to be drawn. it's a good place to set up the canvas and
                // to pass the canvas size to the particle system
                //
                // save a reference to the particle system for use in the .redraw() loop
                particleSystem = system

                // inform the system of the screen dimensions so it can map coords for us.
                // if the canvas is ever resized, screenSize should be called again with
                // the new dimensions
                particleSystem.screenSize(canvas.width, canvas.height)
                particleSystem.screenPadding(80) // leave an extra 80px of whitespace per side

                // set up some event handlers to allow for node-dragging
                that.initMouseHandling()
            },

            redraw:function(){
                //
                // redraw will be called repeatedly during the run whenever the node positions
                // change. the new positions for the nodes can be accessed by looking at the
                // .p attribute of a given node. however the p.x & p.y values are in the coordinates
                // of the particle system rather than the screen. you can either map them to
                // the screen yourself, or use the convenience iterators .eachNode (and .eachEdge)
                // which allow you to step through the actual node objects but also pass an
                // x,y point in the screen's coordinate system

                if (nodes_ready){
                    ctx.fillStyle = "Cornsilk"
                    ctx.fillRect(0,0, canvas.width, canvas.height)

                    particleSystem.eachEdge(function(edge, pt1, pt2){
                        // edge: {source:Node, target:Node, length:#, data:{}}
                        // pt1: {x:#, y:#} source position in screen coords
                        // pt2: {x:#, y:#} target position in screen coords

                        // draw a line from pt1 to pt2
                        ctx.strokeStyle = "rgba(0,0,0, .333)"
                        ctx.lineWidth = 1
                        ctx.beginPath()
                        ctx.moveTo(pt1.x, pt1.y)
                        ctx.lineTo(pt2.x, pt2.y)
                        ctx.stroke()
                        ctx.fillStyle = 'black';
                        console.out(edge)
                        ctx.fillText(edge.data["type"],((pt1.x+pt2.x)/2) + 10,(pt1.y+pt2.y)/2 + 15);
                    })

                    particleSystem.eachNode(function(node, pt){
                        // node: {mass:#, p:{x,y}, name:"", data:{}}
                        // pt: {x:#, y:#} node position in screen coords
                        // draw a rectangle centered at pt
                        var base = 60
                        var height = 20
                        ctx.fillStyle = "black"
                        ctx.fillRect(pt.x-base/2, pt.y-height/2, base,height)
                        ctx.fillStyle = 'white';
                        ctx.fillText(node.name,(pt.x-base/2) + 10,pt.y-height/2 + 15);
                    })

                }
            },

            initMouseHandling:function(){
                // no-nonsense drag and drop (thanks springy.js)
                var dragged = null;

                // set up a handler object that will initially listen for mousedowns then
                // for moves and mouseups while dragging
                var handler = {
                    clicked:function(e){
                        var pos = $(canvas).offset();
                        _mouseP = arbor.Point(e.pageX-pos.left, e.pageY-pos.top)
                        var new_root = particleSystem.nearest(_mouseP).node.name;
                        
                        
                        particleSystem.prune(function(node, from, to){
                            return true;
                        })
                        loadNodes(particleSystem, new_root)
                        
                        return false
                    },
                    dragged:function(e){
                        
                        return false
                    },

                    dropped:function(e){
                        
                        return false
                    }
                }

                // start listening
                $(canvas).mousedown(handler.clicked);

            },

        }
        return that
    }

    function search(){
        var sys = arbor.ParticleSystem(1000, 600, 0.5) // create the system with sensible repulsion/stiffness/friction
        sys.parameters({gravity:true}) // use center-gravity to make the graph settle nicely (ymmv)
        sys.renderer = Renderer("#viewport") // our newly created renderer will have its .init() method called shortly by sys...
        var root = document.getElementById("search-text").value
        loadNodes(sys, root)
    }

    $(document).ready(function(){
        
        document.getElementById("search-button").onclick = search;
        // add some nodes to the graph and watch it go...
        
        // or, equivalentl

    })

    function loadNodes(system, root){
        //Calls to api
        var node_root = null
        $.ajax({
            url: "api/v1/concept/"+root,
            context: document.body,
            type:"get",
            async:false,
            dataType: "json",
            success: function(data, response){
                node_root = system.addNode(data.label, {mass:1.0, fixed:true, description:data.description})
                for(var i = 0; i<data.links.length; i++){
                    if(data.links[i].label != ""){
                        system.addNode(data.links[i].label, {mass:1.0, description:""})
                        system.addEdge(root, data.links[i].label,{length:0.3,type:data.links[i].type})
                    }                
            }
            var box = document.getElementById("user-box")
            box.style.display="none"
            }
        })

/*        $.ajax({
            url: "api/v1/concept/?format=json&neighbor="+root,
            context: document.body,
            type:"get",
            async:false,
            dataType: "json",
            success: function(data, response){
                objects = data.objects
                
                for(var i = 0; i<objects.length; i++){
                    system.addNode(objects[i].label, {mass:1.0, description:objects[0].description})
                    links = objects[i].links
                    for(var j = 0; j<links.length; j++){
                        if(links[j].label === root){
                            system.addEdge(root, objects[i].label,{length:0.3,type:links[j].type})
                        }
                    }
                }
                        
            }
        })*/
                        //first For loop create nodes
                        /*
	  	var node = new Node(label, {mass:1.0, description:description})
	  	system.addNode(node)

	  //second loop link Nodes
	  	system.addEdge(system.geNode(label1), system.geNode(label2),{type:type})
                         */
    }

})(this.jQuery)

