
import pandas as pd
import os
import re

def combine_army_data():
    army_folder = "army"
    combined_output_file = os.path.join(army_folder, "war_dead_data_army_combined.xlsx")
    
    all_names = []

    print(f"Reading Excel files from {army_folder}...")
    # Get all Excel files in the army folder, sorted by part number
    excel_files = [f for f in os.listdir(army_folder) if f.startswith("war_dead_data_army_part_") and f.endswith(".xlsx")]
    
    # Sort files numerically based on the part number
    excel_files.sort(key=lambda f: int(re.search(r'part_(\d+)', f).group(1)))

    for filename in excel_files:
        file_path = os.path.join(army_folder, filename)
        try:
            df = pd.read_excel(file_path)
            # Assuming the name column is 'Name' based on previous scraping
            if 'Name' in df.columns:
                all_names.extend(df['Name'].tolist())
            else:
                print(f"Warning: 'Name' column not found in {filename}. Skipping.")
        except Exception as e:
            print(f"Error reading {filename}: {e}")

    print(f"Total names collected from existing files: {len(all_names)}")

    # --- Custom Excel Formatting ---
    if all_names:
        excel_data = []
        row_data = []
        for i, name in enumerate(all_names):
            row_data.append(i + 1) # Sequential number
            row_data.append(name) # Soldier's name
            
            if len(row_data) == 20: # 10 pairs of (number, name)
                excel_data.append(row_data)
                row_data = []
        
        # Add any remaining data if the total count is not a multiple of 10
        if row_data:
            # Pad with empty strings if the last row is not full
            while len(row_data) < 20:
                row_data.append('') 
            excel_data.append(row_data)

        df_combined = pd.DataFrame(excel_data)
        try:
            # Save without header and index
            df_combined.to_excel(combined_output_file, index=False, header=False)
            print(f"Combined Army data successfully saved to {combined_output_file}")
        except Exception as e:
            print(f"Error saving combined Army data to Excel: {e}")
    else:
        print("No names were collected to combine.")

if __name__ == "__main__":
    combine_army_data()
