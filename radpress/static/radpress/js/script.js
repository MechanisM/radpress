/* Dear contributor, this code snippet is required to resize pre tag for
 * article div width. If you have a better idea about using horizontal
 * scrolling in pre, please fork radpress repository from github, and send me
 * pull request with your changes. thanks.
 */

var articleDiv = $('.article');
var articleContentDiv = $('.article-content');
var highlighttable = $('td.code pre');

if (highlighttable) {
    var preWidth;
    var spaces = parseInt(articleDiv.css('padding-left').split('px')[0])
               + $('td.linenos').width();
    console.log(spaces);

    $(window).on('load resize', function() {
        preWidth = articleContentDiv.width() - spaces;
        $('td.code pre').css('width', preWidth);
    });
}
