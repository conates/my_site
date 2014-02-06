$(function() {

	var Page = (function() {
		var $navArrows = $( '#nav-arrows' ),
			$nav = $( '#nav-dots > span' ),
			slitslider = $( '#slider' ).slitslider( {
				onBeforeChange : function( slide, pos ) {
					$nav.removeClass( 'nav-dot-current' );
					$nav.eq( pos ).addClass( 'nav-dot-current' );
				}
			} ),
			init = function() {
				initEvents();
			},
			initEvents = function() {
				// add navigation events
				$navArrows.children( ':last' ).on( 'click', function() {
					slitslider.next();
					return false;
				});
				$navArrows.children( ':first' ).on( 'click', function() {
					slitslider.previous();
					return false;
				});

				$( '#nav-dots > span:first').nextAll().removeClass( 'nav-dot-current' );
				
				$nav.each( function( i ) {
					$( this ).on( 'click', function( event ) {
						var $dot = $( this );
						if( !slitslider.isActive() ) {
							$nav.removeClass( 'nav-dot-current' );
							$dot.addClass( 'nav-dot-current' );
						}
						slitslider.jump( i + 1 );
						return false;
					} );
				});
				/*Menu home*/
				$(".wheel-button").wheelmenu({
					trigger: "hover",
					animation: "fly",
					animationSpeed: "fast"
				});
				$(".sl-slide .description").hover(function() {
					$(this).siblings('.info').css('top','0px');
				}, function() {
					$(this).siblings('.info').css('top','-500px');
				});
			};
			return { init : init };
	})();
	Page.init();
});