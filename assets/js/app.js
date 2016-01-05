/**
 * Created by Job on 12/28/2015.
 */
$(function(){
   $('#q').autocomplete({
        source: function (request, response) {
            $.getJSON("/autocomplete/?q=" + request.term, function (data) {
                response($.map(data, function (value, key) {
                    return {
                                label: value,
                                value: key
                             };
                    }));
            });
        },
       minLength: 1
    });
});
