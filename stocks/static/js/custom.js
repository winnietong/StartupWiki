$(document).ready(function(){

    var company = {};

    $('.search_input').keypress(function(e){
       if(e.which==13){
           initialize_request();
       }
    });

    // On search button click, change url
    $('.search_button').on('click', function(){
        initialize_request();
    });

    function initialize_request(){
        var val = $('.search_input').val();
        var root_url = window.location.host;
        window.location.href = "http://" + root_url + "/search/?q=" + val;
        // Get the query
        request_url = "https://api.angel.co/1/search?query=" + val + "&type=Startup";
        angellist_get(request_url);
    }

    function initialize(){
        var val = $('.search_input').val();
        if (val === '') val = $('.search_input').attr('placeholder');

        // get url query
        request_url = "https://api.angel.co/1/search?query=" + val + "&type=Startup";
        angellist_get(request_url);
    }

    // show all images on page
    function angellist_get(url){
        console.log(url);
        $.ajax({
            url: url,
            type: "GET",
            dataType: "jsonp",
            success: function(data) {
                for(i=0; i<2; i++){
                    get_each_company(data[i].id);
                }
            },
            error: function(response){
                console.log(response);
            }
        });
    }

    function get_each_company(angellist_id){
        var url =  "https://api.angel.co/1/startups/" + angellist_id;
        $.ajax({
            url: url,
            type: "GET",
            dataType: "jsonp",
            success: function(response){
                var companyinfo = response;
                company = {
                    'name': companyinfo.name,
                    'image': companyinfo.logo_url,
                    'city': companyinfo.locations[0].display_name,
                    'description': companyinfo.product_desc
                };
                show_company(company);
                console.log(company);
            },
            error: function(response){
            }
        });
    }

    function show_company(company){
        company = JSON.stringify(company);
        $.ajax({
            url: '/show_company/',
            type: 'POST',
            dataType: 'html',
            data: company,
            success: function(response) {
                console.log("OK");
                $('.search_results').append(response);
            },
            error: function(error_response) {
                console.log(error_response);
            }
        })
    }

    initialize();
});
