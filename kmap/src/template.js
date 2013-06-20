/*
    Template that shows the design recommendations be followed when make a new
    module or tool within eAros project.

    As we are developing a module, only include a description of the same.
    
    Tag Description
    
    @author         Author's name
    @constructor    Show the constructor
    @deprecated     Show it's a deprecated method
    @exception      the same like @throws
    @param          methods's parameters
    @private        show private method
    @return         show what's returned
    @see            show asociation with a different object
    @throws         show method's exceptions
    @version        show version's number

*/

/*
    This function does something see example below:
    @example
    var x = foo("test"); //it will show "test" message

    @param {string} str: string argumnet that will be shown in message
 */
function foo(str)
{
   alert(str);
}


/*
    Shape is an abstract base class. It is defined simply
    to have something to inherit from for geometric
    subclasses
    @constructor
*/
function Shape(color){
    this.color = color;
}
     
// Bind the Shape_getColor method to the Shape class
Shape.prototype.getColor = Shape_getColor;
 
/*
    Get the name of the color for this shape
    @returns A color string for this shape
*/
function Shape_getColor(){
    return this.color;
}
 
/*
    Circle is a subclass of Shape
*/
function Circle(radius){
    this.radius = radius;
}
 
/*
    A very rough value for pi
*/
Circle.PI = 3.14;
 
/*
    Get the radius of this circle
    @returns The radius of this circle
*/
function Circle_getRadius(){
    return this.radius;
}
 
// Circle is a subclass of Shape
Circle.prototype = new Shape(null);