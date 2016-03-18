(function() {
    'use strict';
    var progression = ['ArrowUp','ArrowUp','ArrowDown','ArrowDown','ArrowLeft','ArrowRight','ArrowLeft','ArrowRight','KeyB','KeyA','Enter'];
    var progression_position = 0

    window.addEventListener('keydown', function (event) {
        if (event.defaultPrevented) {
            return; // Should do nothing if the key event was already consumed.
        }
        if(progression[progression_position]===event.code){
            progression_position++
            console.log('Progress '+progression_position);
            if(progression_position>=progression.length){
                var classes = document.getElementsByClassName('control-lock');
                Array.prototype.forEach.call(classes, function(element){
                    element.style.display='inline';
                });
            }
        }else{
            progression_position=0;
        }
    });  
})();
