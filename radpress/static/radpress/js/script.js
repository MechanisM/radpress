/* Dear contributor, this code snippet is required to resize pre tag for 
 * article div width. If you have a better idea about using horizontal 
 * scrolling in pre, please fork radpress repository from github, and send me
 * pull request with your changes. thanks.
 */

var articleDiv = $('.article');

if (articleDiv) {
	var preWidth;

	$(window).on('load resize', function() {
		preWidth = $('.highlight pre').width() - $('td.linenos').width();
		$('td.code pre').css('width', preWidth);
	});
}
