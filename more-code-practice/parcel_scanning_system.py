
'''
Parcel Scanning System
You are automating a parcel scanning system in a warehouse. Each parcel has a barcode. The system must validate all parcels and report issues:
Tasks:
There is list named parcel_code which consist of barcods.
The system will go through each barcode in the list using a for loop:
If a barcode is "DAMAGED", skip it using continue and log: "Skipped damaged parcel".
If a barcode is "STOP", use break and log: "Critical error: Stopping scan".
For valid barcodes, log: "Scanned parcel: <barcode>".
If the loop completes without hitting a break, log: "All parcels scanned successfully" using for-else.
Return a list of all scan messages.
'''

# This function will be tested automatically.
# Do not change the function name or parameters.
def scan_parcels(parcel_codes: list[str]) -> list[str]:
    scan_messages = []
    for barcode in parcel_codes:
        if barcode == "DAMAGED":
            scan_messages.append("Skipped damaged parcel")
            continue
        elif barcode == "STOP":
            scan_messages.append("Critical error: Stopping scan")  
            break
        else:
            scan_messages.append(f"Scanned parcel: {barcode}")
    else:
        scan_messages.append("All parcels scanned successfully")
    
    return scan_messages 