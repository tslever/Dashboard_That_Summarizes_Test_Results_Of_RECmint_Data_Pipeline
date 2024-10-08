from dash import html
from dashboard.Creator_Of_Table import create_of_table
from dashboard.Details import Details


class Creator_Of_Details():


    def create_details_of_table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID(self):
        details_with_table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID = Details(
            summary = "Table Of Indices Of Rows In Table Generators With Missing GATS ID",
            table = create_of_table.create_table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID()
        )
        return details_with_table_of_indices_of_rows_in_table_Generators_with_missing_GATS_ID


    def create_details_of_table_of_samples_of_table_Generators(self):
        details_with_table_of_samples_of_table_Generators = Details(
            summary = "Table Of Samples Of Table Generators",
            table = create_of_table.create_table_of_samples_of_table_Generators()
        )
        return details_with_table_of_samples_of_table_Generators


    def create_details_of_table_of_statistics_of_table_Generators(self):
        details_with_table_of_statistics_of_table_Generators = Details(
            summary = "Table Of Statistics Of Table Generators",
            table = create_of_table.create_table_of_statistics_of_table_Generators()
        )
        return details_with_table_of_statistics_of_table_Generators


    def create_details_of_table_of_visualizations_of_quantity(
        self,
        quantity_in_AirTable: str,
        quantity_in_RECBus: str,
        log_should_be_applied: bool
    ):
        details_with_table_of_visualizations_of_quantity = Details(
            summary = f"Table Of Visualizations Of {quantity_in_AirTable} and {quantity_in_RECBus}",
            table = create_of_table.create_table_of_visualizations_of_quantity(quantity_in_AirTable = quantity_in_AirTable, quantity_in_RECBus = quantity_in_RECBus, log_should_be_applied = log_should_be_applied),
            indentation = 20
        )
        return details_with_table_of_visualizations_of_quantity
    

    def create_details_of_details_of_tables_of_visualizations_of_quantity(self):
        details_of_details_of_visualizations = html.Details(
            children = [
                html.Summary("Details Of Details Of Visualizations"),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "AC Capacity (kW AC)", quantity_in_RECBus = "nominal-power-AC", log_should_be_applied = True),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "AP to Date", quantity_in_RECBus = None, log_should_be_applied = True),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Average Cost/REC", quantity_in_RECBus = None, log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "COUNT - Contracts", quantity_in_RECBus = None, log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Contract Term Length", quantity_in_RECBus = None, log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Count - Gen Sync Not Computed", quantity_in_RECBus = None, log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Lifetime RECs", quantity_in_RECBus = None, log_should_be_applied = True),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Locked Annuity Rate for Current Contract", quantity_in_RECBus = None, log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "M&S - Fee%", quantity_in_RECBus = None, log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Nameplate (kW DC)", quantity_in_RECBus = "nominal-power", log_should_be_applied = True),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Qty Unpurchased RECs", quantity_in_RECBus = None, log_should_be_applied = True),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "STT1 Revenue", quantity_in_RECBus = None, log_should_be_applied = True),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Specific Yield (given)", quantity_in_RECBus = None, log_should_be_applied = True),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "TEMP - GenSync row mismatch (expected RECs", quantity_in_RECBus = None, log_should_be_applied = True),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Y1 RECs (calc)", quantity_in_RECBus = None, log_should_be_applied = True),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Year Contract Signed", quantity_in_RECBus = None, log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Zip Code", quantity_in_RECBus = "address/zipcode", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "Modeled Y1 RECs", quantity_in_RECBus = None, log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = "VA LIQP", quantity_in_RECBus = None, log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "utility/id", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/0/index", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/0/tilt", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/0/orientation", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/0/module-count", log_should_be_applied = True),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/0/module-power-rating", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/1/index", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/1/tilt", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/1/orientation", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/1/module-count", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/1/module-power-rating", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/2/index", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/2/tilt", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/2/orientation", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/2/module-count", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/2/module-power-rating", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "balancing-authority/code", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/3/index", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/3/tilt", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/3/orientation", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/3/module-count", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/3/module-power-rating", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/4/index", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/4/tilt", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/4/orientation", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/4/module-count", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/4/module-power-rating", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/5/index", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/5/tilt", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/5/orientation", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/5/module-count", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/5/module-power-rating", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/6/index", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/6/tilt", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/6/orientation", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/6/module-count", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/6/module-power-rating", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/7/index", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/7/tilt", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/7/orientation", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/7/module-count", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/7/module-power-rating", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/8/index", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/8/tilt", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/8/orientation", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/8/module-count", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/8/module-power-rating", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/9/index", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/9/tilt", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/9/orientation", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/9/module-count", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/9/module-power-rating", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/10/index", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/10/tilt", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/10/orientation", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/10/module-count", log_should_be_applied = False),
                self.create_details_of_table_of_visualizations_of_quantity(quantity_in_AirTable = None, quantity_in_RECBus = "arrays/10/module-power-rating", log_should_be_applied = False)
            ]
        )
        return details_of_details_of_visualizations


creator_of_details = Creator_Of_Details()