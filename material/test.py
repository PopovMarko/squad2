
            <thead class = "thead-dark" >
               <tr >
                    <th scope = "col" >№</th >
                    <th scope = "col" > Найменування < /th >
                    <th scope = "col" > Кількість < /th >
                </tr>
            </thead>
            <tbody>
                {% for i in formset %}
                {% csrf_token %}
                {{ formset.management_form }}
                {{i.as_table}}
                <tr>
                    <th scope = "row">{{ forloop.counter }}</th>
                    <td scope = "row"> {{ i.goods_ref }}</a></td>
                    <td scope = "row"> {{ i.quantity }}</td>
                    <td scope = "row"> {{ i.consignment_ref }}</td>
                </tr>
                {% endfor %}
            </tbody>
