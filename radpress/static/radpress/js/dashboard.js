$("a.article-delete").on('click', function() {
    return confirm(window.confirmDeletionMessage);
});

$('#dashboard-tabs a:first').tab('show');