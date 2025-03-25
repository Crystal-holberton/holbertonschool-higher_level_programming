import os

def generate_invitations(template, attendees):
    """Generates personalized invitation files from a template"""
    # Validate input types
    if not isinstance(template, str):
        print("Error:Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    # Handle empty inputs
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    # Process each attendee and generate output files
    for index, attendee in enumerate(attendees, start=1):
        # Replace missing values with 'N/A'
        processed_template = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A") or "N/A"
            processed_template = processed_template.replace(f"{{{key}}}", value)
        # Write to output file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, "w") as output_file:
                output_file.write(processed_template)
            print(f"Generated: {output_filename}")
        except IOError as e:
            print(f"Error writing to {output_filename}: {e}")
