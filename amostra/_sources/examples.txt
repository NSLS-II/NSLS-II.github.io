More Examples
===================

A Simple Application from LIX
******************************

*Credit: Hugo H. Slepicka*

.. code:: python

    import amostra
    import pandas
    import amostra.client.commands as acc
    import collections

.. code:: python

    # Definitions
    owner = "hhslepicka"
    project = "12345"
    beamline_id = "lix"

.. code:: python

    # Create Handlers for collections of interest for this app
    container_ref = acc.ContainerReference()
    sample_ref = acc.SampleReference()

.. code:: python

    # Simple utility routines for insertion
    def insert_plate(plate_info):
        plate = container_ref.create(**plate_info)
        return plate
    
    def insert_sample_list(samples):
        result = sample_ref.create_sample_list(samples)
        return result

.. code:: python

    # Plate generate factory
    def generate_plate(owner, project, beamline_id, kind, name, barcode, content):
        plate_info = {    
                "owner": owner,
                "project": project,
                "beamline_id": beamline_id,
                "kind": kind,
                "name": name,
                "barcode": barcode,
                "content": list(content)
        }
    
        return insert_plate(plate_info)
    
    # Sample generate factory
    def generate_samples_96wp(project, beamline_id, owner, name):
        samples = collections.deque()
        for i in range(96):
            sample_info = {
                "project": project,
                "beamline_id": beamline_id,
                "owner": owner,
                "name": name+" {}".format(i+1),
                "position": {"x": int(i % 8), "y": int(i/8)},
                "concentration": 0.001,
                "volume": 10,
                "temperature": 21.4    
            }
            samples.append(sample_info)
        uids = insert_sample_list(samples)
        return uids
    
    # A utility function that searches container by user define info
    def find_plate_by_barcode(owner, project, beamline_id, barcode):
        samples = collections.deque()
        plate_info = list(container_ref.find(owner=owner, project=project, beamline_id=beamline_id, barcode=barcode))[0]
        for s_uid in plate_info['content']:
            samples.append(next(sample_ref.find(uid=s_uid)))
        
        plate_info['content'] = list(samples)
        return plate_info

.. code:: python

    number_of_plates = 1

.. code:: python

    # Generate a single plate and fill with samples
    for i in range(number_of_plates):
        samples = generate_samples_96wp(project, beamline_id, owner, "Test Sample")
        plate1 = generate_plate(owner, project, beamline_id, "96wp", "Plate {}".format(i+1), "{}".format(i+1).zfill(13), samples)

.. code:: python

    # Excel utility function using pandas
    # Fill up the container and sample information from excel
    
    def import_plate_from_excel(fname, owner, project, beamline_id, plate_kind):
        samples = collections.deque()
        excel_data = pandas.read_excel(fname,header=1)
        
        for line in excel_data.iterrows():
            if line[0] == 0:
                name = line[1][0]
                barcode = str(int(line[1][1])).zfill(13)
                plate_info = {    
                    "owner": owner,
                    "project": project,
                    "beamline_id": beamline_id,
                    "kind": plate_kind,
                    "name": name,
                    "barcode": barcode,
                }
            s_x = line[1][2]
            s_y = line[1][3]
            s_name = line[1][4]
            s_shortname = line[1][5]
            s_conc = line[1][6]
            s_volume = line[1][7]
            s_temperature = line[1][8]
            sample_info = {
                    "project": project,
                    "beamline_id": beamline_id,
                    "owner": owner,
                    "name": s_name,
                    "short_name": s_shortname,
                    "position": {"x": s_x, "y": s_y},
                    "concentration": s_conc,
                    "volume": s_volume,
                    "temperature": s_temperature        
                }
            samples.append(sample_info)
            
        return plate_info, samples

.. code:: python

    excel_file = "Sample_Import.xlsx"
    plate, samples = import_plate_from_excel(excel_file, owner, project, beamline_id, "96wp")

.. code:: python

    content = insert_sample_list(samples)
    plate['content'] = content
    
    # Send the prepared data to the server
    inserted_plate = insert_plate(plate)

.. code:: python

    inserted_plate




.. parsed-literal::

    {'barcode': '1000000000001',
     'beamline_id': 'lix',
     'content': ['e13b9a6f-6838-4dbd-b13e-5b67f325c27c',
      'a04ab8ea-83b2-495c-8f3e-7f713d325bae',
      '9ce22068-a27e-4c5f-9911-c46bdb2fc1ed',
      '1bae2551-79d2-4fa4-a9f1-b83ee9f77e6f',
      'cb0267fe-8e62-4831-afd4-1efb658005a8',
      'f136c707-8b32-4352-a728-257762827c1d',
      '1cfd8535-ff1a-4a24-b227-bb21b1cc6d31',
      '1b77ff58-794e-49f5-ba7b-8320c4fda7b1',
      '7618950b-edb3-430b-bfd3-996e74e73838',
      '7454330a-4b5c-4c96-8b60-431fbd01fe0a',
      'f74c9699-09ed-4fb1-8e82-2037b4d621fd',
      'd3cf7987-7c37-411b-bc94-8f95a65ede9c',
      '2667613d-f918-4cf5-a6b2-83f36b2eea65',
      'e1d7b959-0cb6-4a29-a0eb-bd5aed91febc',
      '4eecbdba-c63c-466b-b4c9-83fdbff0e039',
      'e31d4395-f3e1-4a39-aea0-c808505290b5'],
     'kind': '96wp',
     'name': 'Imported Plate',
     'owner': 'hhslepicka',
     'project': '12345',
     'time': 1461338342.433393,
     'uid': '2f3fdd93-fc5a-41d4-968a-45f50e09b473'}



.. code:: python

    # Query the database for the barcode 
    r = find_plate_by_barcode(owner, project, beamline_id, "1000000000001".zfill(13))

.. code:: python

    r["name"]




.. parsed-literal::

    'Imported Plate'



.. code:: python

    # Iterate over the results and print contents inserted then queried
    for sample in r["content"]:
        print("Sample Data: ", sample)


.. parsed-literal::

    Sample Data:  {'beamline_id': 'lix', 'concentration': 0.775, 'name': 'Sample Imp 1-1', 'position': {'x': 1, 'y': 1}, 'short_name': 'S1-1', 'uid': 'e13b9a6f-6838-4dbd-b13e-5b67f325c27c', 'volume': 10, 'time': 1461338342.344707, 'temperature': 21, 'owner': 'hhslepicka', 'project': '12345'}
    Sample Data:  {'beamline_id': 'lix', 'concentration': 0.772, 'name': 'Sample Imp 1-2', 'position': {'x': 1, 'y': 2}, 'short_name': 'S1-2', 'uid': 'a04ab8ea-83b2-495c-8f3e-7f713d325bae', 'volume': 10, 'time': 1461338342.351725, 'temperature': 21, 'owner': 'hhslepicka', 'project': '12345'}
    Sample Data:  {'beamline_id': 'lix', 'concentration': 0.776, 'name': 'Sample Imp 1-3', 'position': {'x': 1, 'y': 3}, 'short_name': 'S1-3', 'uid': '9ce22068-a27e-4c5f-9911-c46bdb2fc1ed', 'volume': 10, 'time': 1461338342.357494, 'temperature': 21, 'owner': 'hhslepicka', 'project': '12345'}
    Sample Data:  {'beamline_id': 'lix', 'concentration': 0.47500000000000003, 'name': 'Sample Imp 1-4', 'position': {'x': 1, 'y': 4}, 'short_name': 'S1-4', 'uid': '1bae2551-79d2-4fa4-a9f1-b83ee9f77e6f', 'volume': 10, 'time': 1461338342.362703, 'temperature': 21, 'owner': 'hhslepicka', 'project': '12345'}
    Sample Data:  {'beamline_id': 'lix', 'concentration': 0.441, 'name': 'Sample Imp 1-5', 'position': {'x': 1, 'y': 5}, 'short_name': 'S1-5', 'uid': 'cb0267fe-8e62-4831-afd4-1efb658005a8', 'volume': 10, 'time': 1461338342.36843, 'temperature': 21, 'owner': 'hhslepicka', 'project': '12345'}
    Sample Data:  {'beamline_id': 'lix', 'concentration': 0.788, 'name': 'Sample Imp 1-6', 'position': {'x': 1, 'y': 6}, 'short_name': 'S1-6', 'uid': 'f136c707-8b32-4352-a728-257762827c1d', 'volume': 10, 'time': 1461338342.374143, 'temperature': 21, 'owner': 'hhslepicka', 'project': '12345'}
    Sample Data:  {'beamline_id': 'lix', 'concentration': 0.9580000000000001, 'name': 'Sample Imp 1-7', 'position': {'x': 1, 'y': 7}, 'short_name': 'S1-7', 'uid': '1cfd8535-ff1a-4a24-b227-bb21b1cc6d31', 'volume': 10, 'time': 1461338342.379789, 'temperature': 21, 'owner': 'hhslepicka', 'project': '12345'}
    Sample Data:  {'beamline_id': 'lix', 'concentration': 0.48, 'name': 'Sample Imp 1-8', 'position': {'x': 1, 'y': 8}, 'short_name': 'S1-8', 'uid': '1b77ff58-794e-49f5-ba7b-8320c4fda7b1', 'volume': 10, 'time': 1461338342.38548, 'temperature': 21, 'owner': 'hhslepicka', 'project': '12345'}
    Sample Data:  {'beamline_id': 'lix', 'concentration': 0.317, 'name': 'Sample Imp 2-1', 'position': {'x': 2, 'y': 1}, 'short_name': 'S2-1', 'uid': '7618950b-edb3-430b-bfd3-996e74e73838', 'volume': 10, 'time': 1461338342.39114, 'temperature': 21, 'owner': 'hhslepicka', 'project': '12345'}
    Sample Data:  {'beamline_id': 'lix', 'concentration': 0.459, 'name': 'Sample Imp 2-2', 'position': {'x': 2, 'y': 2}, 'short_name': 'S2-2', 'uid': '7454330a-4b5c-4c96-8b60-431fbd01fe0a', 'volume': 10, 'time': 1461338342.396493, 'temperature': 21, 'owner': 'hhslepicka', 'project': '12345'}
    Sample Data:  {'beamline_id': 'lix', 'concentration': 0.248, 'name': 'Sample Imp 2-3', 'position': {'x': 2, 'y': 3}, 'short_name': 'S2-3', 'uid': 'f74c9699-09ed-4fb1-8e82-2037b4d621fd', 'volume': 10, 'time': 1461338342.402075, 'temperature': 21, 'owner': 'hhslepicka', 'project': '12345'}
    Sample Data:  {'beamline_id': 'lix', 'concentration': 0.39, 'name': 'Sample Imp 2-4', 'position': {'x': 2, 'y': 4}, 'short_name': 'S2-4', 'uid': 'd3cf7987-7c37-411b-bc94-8f95a65ede9c', 'volume': 10, 'time': 1461338342.407314, 'temperature': 21, 'owner': 'hhslepicka', 'project': '12345'}
    Sample Data:  {'beamline_id': 'lix', 'concentration': 0.5740000000000001, 'name': 'Sample Imp 2-5', 'position': {'x': 2, 'y': 5}, 'short_name': 'S2-5', 'uid': '2667613d-f918-4cf5-a6b2-83f36b2eea65', 'volume': 10, 'time': 1461338342.412499, 'temperature': 21, 'owner': 'hhslepicka', 'project': '12345'}
    Sample Data:  {'beamline_id': 'lix', 'concentration': 0.799, 'name': 'Sample Imp 2-6', 'position': {'x': 2, 'y': 6}, 'short_name': 'S2-6', 'uid': 'e1d7b959-0cb6-4a29-a0eb-bd5aed91febc', 'volume': 10, 'time': 1461338342.417716, 'temperature': 21, 'owner': 'hhslepicka', 'project': '12345'}
    Sample Data:  {'beamline_id': 'lix', 'concentration': 0.371, 'name': 'Sample Imp 2-7', 'position': {'x': 2, 'y': 7}, 'short_name': 'S2-7', 'uid': '4eecbdba-c63c-466b-b4c9-83fdbff0e039', 'volume': 10, 'time': 1461338342.422936, 'temperature': 21, 'owner': 'hhslepicka', 'project': '12345'}
    Sample Data:  {'beamline_id': 'lix', 'concentration': 0.099, 'name': 'Sample Imp 2-8', 'position': {'x': 2, 'y': 8}, 'short_name': 'S2-8', 'uid': 'e31d4395-f3e1-4a39-aea0-c808505290b5', 'volume': 10, 'time': 1461338342.428122, 'temperature': 21, 'owner': 'hhslepicka', 'project': '12345'}


