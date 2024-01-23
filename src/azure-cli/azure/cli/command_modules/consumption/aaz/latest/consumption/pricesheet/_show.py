# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "consumption pricesheet show",
    is_preview=True,
)
class Show(AAZCommand):
    """Show the price sheet for an Azure subscription within a billing period.
    """

    _aaz_info = {
        "version": "2023-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.billing/billingperiods/{}/providers/microsoft.consumption/pricesheets/default", "2023-05-01"],
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.consumption/pricesheets/default", "2023-05-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.billing_period_name = AAZStrArg(
            options=["-p", "--billing-period-name"],
            help="Name of the billing period to get the price sheet.",
            id_part="name",
        )
        _args_schema.expand = AAZStrArg(
            options=["--expand"],
            help="May be used to expand the properties/meterDetails within a price sheet. By default, these fields are not included when returning price sheet.",
        )
        _args_schema.skiptoken = AAZStrArg(
            options=["--skiptoken"],
            help="Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.",
        )
        _args_schema.top = AAZIntArg(
            options=["-t", "--top"],
            help="Maximum number of items to return. Value range: 1-1000.",
            fmt=AAZIntArgFormat(
                maximum=1000,
                minimum=1,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.billing_period_name) is not True
        condition_1 = has_value(self.ctx.args.billing_period_name) and has_value(self.ctx.subscription_id)
        if condition_0:
            self.PriceSheetGet(ctx=self.ctx)()
        if condition_1:
            self.PriceSheetGetByBillingPeriod(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class PriceSheetGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.Consumption/pricesheets/default",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$expand", self.ctx.args.expand,
                ),
                **self.serialize_query_param(
                    "$skiptoken", self.ctx.args.skiptoken,
                ),
                **self.serialize_query_param(
                    "$top", self.ctx.args.top,
                ),
                **self.serialize_query_param(
                    "api-version", "2023-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.tags = AAZDictType(
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            properties.pricesheets = AAZListType(
                flags={"read_only": True},
            )

            pricesheets = cls._schema_on_200.properties.pricesheets
            pricesheets.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.pricesheets.Element
            _element.billing_period_id = AAZStrType(
                serialized_name="billingPeriodId",
                flags={"read_only": True},
            )
            _element.currency_code = AAZStrType(
                serialized_name="currencyCode",
                flags={"read_only": True},
            )
            _element.included_quantity = AAZFloatType(
                serialized_name="includedQuantity",
                flags={"read_only": True},
            )
            _element.meter_details = AAZObjectType(
                serialized_name="meterDetails",
            )
            _element.meter_id = AAZStrType(
                serialized_name="meterId",
                flags={"read_only": True},
            )
            _element.part_number = AAZStrType(
                serialized_name="partNumber",
                flags={"read_only": True},
            )
            _element.unit_of_measure = AAZStrType(
                serialized_name="unitOfMeasure",
                flags={"read_only": True},
            )
            _element.unit_price = AAZFloatType(
                serialized_name="unitPrice",
                flags={"read_only": True},
            )

            meter_details = cls._schema_on_200.properties.pricesheets.Element.meter_details
            meter_details.meter_category = AAZStrType(
                serialized_name="meterCategory",
                flags={"read_only": True},
            )
            meter_details.meter_location = AAZStrType(
                serialized_name="meterLocation",
                flags={"read_only": True},
            )
            meter_details.meter_name = AAZStrType(
                serialized_name="meterName",
                flags={"read_only": True},
            )
            meter_details.meter_sub_category = AAZStrType(
                serialized_name="meterSubCategory",
                flags={"read_only": True},
            )
            meter_details.pretax_standard_rate = AAZFloatType(
                serialized_name="pretaxStandardRate",
                flags={"read_only": True},
            )
            meter_details.total_included_quantity = AAZFloatType(
                serialized_name="totalIncludedQuantity",
                flags={"read_only": True},
            )
            meter_details.unit = AAZStrType(
                flags={"read_only": True},
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200

    class PriceSheetGetByBillingPeriod(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}/providers/Microsoft.Consumption/pricesheets/default",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "billingPeriodName", self.ctx.args.billing_period_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$expand", self.ctx.args.expand,
                ),
                **self.serialize_query_param(
                    "$skiptoken", self.ctx.args.skiptoken,
                ),
                **self.serialize_query_param(
                    "$top", self.ctx.args.top,
                ),
                **self.serialize_query_param(
                    "api-version", "2023-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.tags = AAZDictType(
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            properties.pricesheets = AAZListType(
                flags={"read_only": True},
            )

            pricesheets = cls._schema_on_200.properties.pricesheets
            pricesheets.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.pricesheets.Element
            _element.billing_period_id = AAZStrType(
                serialized_name="billingPeriodId",
                flags={"read_only": True},
            )
            _element.currency_code = AAZStrType(
                serialized_name="currencyCode",
                flags={"read_only": True},
            )
            _element.included_quantity = AAZFloatType(
                serialized_name="includedQuantity",
                flags={"read_only": True},
            )
            _element.meter_details = AAZObjectType(
                serialized_name="meterDetails",
            )
            _element.meter_id = AAZStrType(
                serialized_name="meterId",
                flags={"read_only": True},
            )
            _element.part_number = AAZStrType(
                serialized_name="partNumber",
                flags={"read_only": True},
            )
            _element.unit_of_measure = AAZStrType(
                serialized_name="unitOfMeasure",
                flags={"read_only": True},
            )
            _element.unit_price = AAZFloatType(
                serialized_name="unitPrice",
                flags={"read_only": True},
            )

            meter_details = cls._schema_on_200.properties.pricesheets.Element.meter_details
            meter_details.meter_category = AAZStrType(
                serialized_name="meterCategory",
                flags={"read_only": True},
            )
            meter_details.meter_location = AAZStrType(
                serialized_name="meterLocation",
                flags={"read_only": True},
            )
            meter_details.meter_name = AAZStrType(
                serialized_name="meterName",
                flags={"read_only": True},
            )
            meter_details.meter_sub_category = AAZStrType(
                serialized_name="meterSubCategory",
                flags={"read_only": True},
            )
            meter_details.pretax_standard_rate = AAZFloatType(
                serialized_name="pretaxStandardRate",
                flags={"read_only": True},
            )
            meter_details.total_included_quantity = AAZFloatType(
                serialized_name="totalIncludedQuantity",
                flags={"read_only": True},
            )
            meter_details.unit = AAZStrType(
                flags={"read_only": True},
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]