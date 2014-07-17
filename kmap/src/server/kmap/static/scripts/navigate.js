(function($){
	var system;
	var prox;

    
    function search(root){
        Proxy.getNode(root, loadNodes, handleError)
    }

    $(document).ready(function(){
        
        document.getElementById("search-button").onclick = function(){
        	var root = document.getElementById("search-text").value
        	search(root);
        }
        var canvas_pre = $('#viewport');
        fitToContainer(canvas_pre);
        initializeSystem();

    });
    
    function fitToContainer(canvas){
    	  // Make it visually fill the positioned parent
    	  canvas.css("width", '100%');
    	  canvas.css("height", '100%');
    	  // ...then set the internal size to match
    	  canvas.attr("width", canvas.width());
    	  canvas.attr("height", canvas.height());
    	}
    
    function initializeSystem(){
    	system = arbor.ParticleSystem(1000, 600, 0.5) // create the system with sensible repulsion/stiffness/friction
        system.parameters({gravity:true}) // use center-gravity to make the graph settle nicely (ymmv)
        system.renderer = PreRenderer("#viewport", search) // our newly created renderer will have its .init() method called shortly by sys...
    
        Proxy.init();
    }
    
    function loadNodes(root, data){
        //Calls to api
        var node_root = null
        
        system.prune(function(node, from, to){
            return true;
        })
        
        var base = calculateBase(data.label);
        node_root = system.addNode(data.label, {mass:1.0, fixed:true, description:data.description, root:true, base:base})
        for(var i = 0; i<data.links.length; i++){
            if(data.links[i].label != ""){
            	var base = calculateBase(data.links[i].label);
            	system.addNode(data.links[i].label, {mass:1.0, description:"", base:base})
                system.addEdge(root, data.links[i].label,{length:0.3,type:data.links[i].type})
            }
        }
        
        var box = document.getElementById("user-box")
        box.style.display="none"
    }
    
    function handleError(error){
    	if(error.status == 404){
    		$("#error-box").css("display", "initial")
    	}
    }
    
    function calculateBase(label){
    	var minBase = 60;
    	
    	var base = label.length * 6 + 10
    	
    	return Math.max(minBase, base);
    	
    }


})(this.jQuery)

