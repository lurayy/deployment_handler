
# class BundleClassView(View):
#     @method_decorator(for_everyone())
#     def get(self, request, uuid=None):
#         if uuid:
#             bundle = Bundle.objects.get(uuid=uuid)
#             response_json = {
#                 'status' : True,
#                 'bundle' : bundles_to_json([bundle])[0]
#             }
#             return JsonResponse(response_json)
#         else:
            # start = converter(request.GET.get('start',''))
            # limit = converter(request.GET.get('lmt',''))
            # price_gte = converter(request.GET.get('price_gte',''))
            # price_lte = converter(request.GET.get('price_lte',''))
            # hours_lte = converter(request.GET.get('hours_lte',''))
            # hours_gte = converter(request.GET.get('hours_gte',''))
            # erp_gte = converter(request.GET.get('erp_gte',''))
            # erp_lte = converter(request.GET.get('erp_lte',''))
            # bundles = Bundle.objects.all()
            # if price_gte:
            #     bundles = bundles.filter(price__gte = price_gte)
            # if price_lte:
            #     bundles = bundles.filter(price__lte = price_lte)
            # if hours_gte:
            #     bundles = bundles.filter(hours__gte = hours_gte)
            # if hours_lte:
            #     bundles = bundles.filter(hours__lte = hours_lte)
            # if erp_gte:
            #     bundles = bundles.filter(number_of_erp__gte = erp_gte)
            # if erp_lte:
            #     bundles = bundles.filter(number_of_erp__lte = erp_lte)
            # if start == None:
            #     start = 0
            # if limit == None:
            #     limit = 20
            # bundles = bundles[start:start+limit]
            # return JsonResponse({'status':True, 'bundles': bundles_to_json(bundles)})

#     @method_decorator(for_mods_only())
#     def post(self,request):
#         json_str = request.body.decode(encoding='UTF-8')
#         data_json = json.loads(json_str)
#         bundle = Bundle.objects.create(
#             hours = data_json['hours'],
#             number_of_erp = data_json['number_in_erp'],
#             price = data_json['price']
#         )
#         response_json = {
#             'status' : True,
#             'bundle' : bundles_to_json([bundle])[0]
#         }
#         return JsonResponse(response_json)
    
#     @method_decorator(for_mods_only())
#     def patch(self,request, uuid):
#         if uuid == None:
#             raise Exception('UUID required.')
#         bundle = Bundle.objects.get(uuid=uuid)
#         json_str = request.body.decode(encoding='UTF-8')
#         data_json = json.loads(json_str)
#         if data_json['hours']:
#             bundle.hours = int(data_json['hours'])
#         if data_json['number_of_erp']:
#             bundle.number_of_erp = int(data_json['number_of_erp'])
#         if data_json['price']:
#             bundle.price = int(data_json['price'])
#         response_json = {
#             'status' : True,
#             'bundle' : bundles_to_json([bundle])[0]
#         }
#         return JsonResponse(response_json)
    
#     @method_decorator(for_mods_only())
#     def delete(self, request, uuid):
#         if uuid == None:
#             raise Exception('UUID required.')
#         bundle = Bundle.objects.get(uuid=uuid)
#         bundle.delete()
#         return JsonResponse({'status' : True})
