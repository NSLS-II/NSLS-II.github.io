
.. code:: python

    from amostra.client.commands import SampleReference, RequestReference, ContainerReference
    import uuid

Online Sample Management Examples
=================================

.. code:: python

    # Create a sample reference. This will be used in order to communicate with 
    # the amostra server
    conn = SampleReference()

.. code:: python

    # Create a simple sample and a list of samples, 100 of them
    conn.create(**{'name': 'sample3', 'time': 1461336991.929094, 'container': 'puck2'})
    tmp = []
    for i in range(100):
        tmp.append({'container': 'puck2','name': 'sample{}'.format(i)})
    conn.create_sample_list(tmp)




.. parsed-literal::

    ['f459a2b2-2fb4-4f30-aab4-e0c7b8092473',
     '4342e439-f86f-46a6-96cc-687efccedd62',
     'd689a0fd-48a1-4ccd-ad90-34f541c30c22',
     '292a1cce-499e-4718-a3ba-58340b0bdceb',
     '3c6cef6d-f9e5-4d94-a12f-6194e5bcab19',
     '58d9f680-760f-4aec-a24b-669765dd2426',
     '1f5d0cee-b26c-4063-a4ef-39c2e3b3ab29',
     'cbca0976-a340-4cd6-8ab2-285e9c699b5f',
     '80eb6184-92ea-498a-8634-b3a7dc6981ee',
     'a12a8bf7-eba0-4222-ab2b-59fffb81f3a4',
     'eca6dac2-58c2-41e3-a72d-7eeae886d5da',
     'acae82af-809b-4d74-ba9d-d72b77c5c029',
     '35c42e46-aaa7-4ad7-97a5-e9e39a8a0afd',
     '2a47b21e-0021-47b4-a482-6d79afecafa2',
     '5b1bcebc-4090-434d-82f1-baceb002abed',
     '7c24bf66-9fda-4861-84ec-7ec0ab82354d',
     '51f75927-86b8-4553-83b5-1484d7d8de7c',
     '3680626c-0aaa-49a0-8b88-902e771a42d7',
     '5d9b7439-0f06-4f97-ae19-e05d49c803a5',
     '683415da-386d-4798-aa3c-06a6cae590ac',
     'f5bf695d-4d19-458c-82c7-d71389363550',
     'a43e7f5f-7c6c-4b36-9e04-d426db56b81c',
     '4884d1bd-6191-4382-822f-96bd6f220a75',
     '6d31b764-5214-4d8a-b280-5a9dcc5d16d4',
     'ba1b2be0-d440-4565-8028-d11162a32025',
     '93764f60-bc37-4b43-8cbb-323170a621b9',
     'd3f50bd8-4220-4e8a-a845-982e32ae5d12',
     '28d73a23-3e73-4087-8f87-62014d261e4c',
     '597cf592-dbfb-4e77-a71b-f9285e4ecb10',
     '243305e8-6804-4996-8bfd-f43046ac90f4',
     '80fe0162-ff7d-48bd-99bb-2eea07a0c9c1',
     '4b28dd63-6465-4fb2-bb7e-b676c37d22aa',
     '908bcebc-4d5c-4e88-9464-d7f139a6fd37',
     '2770efbf-314a-48f7-a68a-64c67a3dffe9',
     '351447a1-568c-442c-86f6-0220ebaab128',
     '9e649f66-7ce3-4751-b258-c075daa5f34b',
     '6708441f-4e07-442e-a13b-5e797923a920',
     '9ab40b4d-930d-4543-a608-97ce1444bc1d',
     '19fdb172-ea85-4df0-b505-ec0e6590a86d',
     '9d85d0b8-4307-499e-882e-74ca4c6465c4',
     '46747b9b-f6ab-44b2-a089-ecd6c28dfa8b',
     '7bec8d46-315d-4737-bef5-6d840e3a0574',
     '8132ce2f-ea3d-40e4-b912-f186212a13bb',
     '6ff559ac-6fcd-499d-80bd-e73166eb76bf',
     '55fde6f4-c930-4d4a-b473-3b42302ec3a5',
     '3af8b387-c6ae-498f-add1-1f0eb3af796b',
     'd28dd9e0-79bf-4674-bc62-4e302ccdace5',
     'fbcb291e-6f3e-42cd-83f8-87a71c435159',
     '8bc3daa9-7497-424f-b9ce-5d5e5bebf780',
     '5b015361-6511-4c1c-bd56-0dd7b653e357',
     '39723fd4-471d-4269-af5e-3e2c3725ca2a',
     'fa48d311-efbf-467a-8d3e-adc520f090af',
     'ac3658cf-4807-4412-9673-22adc5aff88c',
     '474107a9-f561-4dc3-8053-92a8b8c821ba',
     '075aafba-dca7-44d6-8e3c-67b966e3574c',
     '48d4045e-ea32-4189-b733-4e5a88a5c9be',
     '78efb679-bfc8-4802-80cd-4d6f40984561',
     'bfa29b7c-4ff4-452b-a00c-ca31a127b807',
     'a5e17639-4396-4967-ae79-dfa194bf92cc',
     'a93aa73e-4112-4be6-8b2a-c260cc235c6e',
     '751adb04-d9c5-49c2-981c-93ce3db91c86',
     '4df2cc18-1075-4c9d-b51a-97dd2ab11831',
     '54c0dbd9-aa8d-4847-9838-444fc08e4d6c',
     '0aa86bd6-86ea-44be-b507-721e6b06d850',
     '4e2f934a-01ea-44ac-80a7-1f3591d859ab',
     '8c29bca5-3817-4761-9fd0-1c8deb59e8a1',
     '46d3304c-c8c5-4550-a3e5-f236253ae414',
     '931e9087-1830-49cb-b878-0e7b2adac375',
     'd56fa80f-0914-4aa7-a850-1e9b38b2c30a',
     '76773f68-5bca-4255-89fa-4e36c147490b',
     '9f477b6e-c7e7-4a1e-9a81-756a63a7908d',
     'baf84af3-8154-4469-a7dd-c1ff930593e8',
     '763061f0-5cba-4dd3-b7cf-0b1682add3f1',
     '23cafa21-0d30-4fe5-b889-3ab5e090f1c4',
     'cff239e9-35c7-4cc8-8028-53cd988afbd4',
     'ddc504dc-35cc-4dee-b8b3-83ea4b2b3be3',
     'd8fa1b1e-33a3-4298-a08e-c64149f36638',
     '106a1af6-3046-4cbc-820f-d56cf914e1ba',
     '67fb1283-9f87-4788-badf-ba2ec35ab669',
     '36817bb0-47b7-4447-a441-fe3ae932ab52',
     '519b30a6-6385-442a-b3e8-4b537ac91a70',
     '78cdb246-465f-424e-aa08-0f1c7b1d242f',
     '55bacf64-909b-4048-bcdd-f3abaf373c44',
     '282f0d36-d4f7-47de-97e7-a770e2db7473',
     'af1dbca2-831b-41ed-bbd0-1ddcfaa95f34',
     '1993ca2b-ceb9-4727-a36a-f0967b16c701',
     'f5dcf66f-53c0-4bb9-be67-55d3db62fdaf',
     '780b9b5e-39c3-46e5-8798-6dcbed663102',
     '74f32c1a-5264-42ad-a07c-c2fbff8a75bf',
     'bfc97a00-bb28-4268-8716-c0a5794623f9',
     '565a13ba-d90e-4f26-9703-5d8959ebc3e2',
     '1f8f8d47-f579-455b-bb28-b27db3278f35',
     '26ed0a92-359d-45ea-be41-53a7eda1a590',
     '70967f09-b7a3-4b16-8a58-bf143d81033a',
     '43965a19-3f86-4d9b-956d-fcbf09c15cf9',
     '192e8001-87c4-4a59-a831-93cb74c0ad87',
     'ebdd422a-3f8c-417f-81f1-8d9ce7808fff',
     '2ddc23b3-4265-4228-bdf2-aa3b8c14b922',
     '4dc9c568-0d27-4471-9b3c-e3c524bf06fc',
     '024449ad-b423-4405-9ac3-97082efb2380']



.. code:: python

    # Update the sample(s) with name=2. Replace which container this sample belongs to
    
    conn.update({'name': 'sample2'}, {'container': 'puck1'})
    
    # True suggests update complete. Else raises




.. parsed-literal::

    True



.. code:: python

    # All 'find()'s return generators
    conn.find()




.. parsed-literal::

    <generator object SampleReference.find at 0x106953570>



.. code:: python

    # Create a handler for container
    conn2 = ContainerReference()

.. code:: python

    # Create a simple container
    conn2.create(container='puck1')




.. parsed-literal::

    {'container': 'puck1',
     'time': 1461595532.861217,
     'uid': 'f62a90d1-5c3e-48d4-a947-4255935a132b'}



.. code:: python

    # Get all containers created
    list(conn2.find())




.. parsed-literal::

    [{'container': 'puck1',
      'time': 1461595532.861217,
      'uid': 'f62a90d1-5c3e-48d4-a947-4255935a132b'},
     {'container': 'puck2',
      'time': 1461349981.393828,
      'uid': 'fce8269b-f3a0-406f-bffe-d65506f25a86'},
     {'container': 'puck2',
      'time': 1461349845.672055,
      'uid': '56606e4e-d47d-4868-9f74-6651ed4e8275'},
     {'container': 'puck2',
      'time': 1461329918.217565,
      'uid': '9930a70c-51a2-46a6-bb14-7efa22a69d9e'},
     {'container': 'puck2',
      'time': 1461275348.307509,
      'uid': 'e4f7e744-91c2-41b3-866c-0ae647cb873d'},
     {'time': 1461275338.994905, 'uid': '6a04517c-9b2f-4a34-a942-f701c251fe94'}]



.. code:: python

    # Update what container puck1 is contained within
    conn2.update({'container': 'puck1'} ,{'container': 'puck2'})




.. parsed-literal::

    True



.. code:: python

    # Create a request handler
    conn3 = RequestReference()

.. code:: python

    # Create a single request with one of the samples (in this case, arbitrary)
    conn3.create(sample=next(conn.find()))




.. parsed-literal::

    {'sample': '024449ad-b423-4405-9ac3-97082efb2380',
     'seq_num': 0,
     'state': 'active',
     'time': 1461595537.429296,
     'uid': '99d56b43-25c9-4e11-97c3-f89d9f88a66e'}



.. code:: python

    # Get the last 10 arbitrary requests
    list(conn3.find())[0:10]




.. parsed-literal::

    [{'sample': '024449ad-b423-4405-9ac3-97082efb2380',
      'seq_num': 0,
      'state': 'active',
      'time': 1461595537.429296,
      'uid': '99d56b43-25c9-4e11-97c3-f89d9f88a66e'},
     {'sample': '249c51e1-ba7f-4412-834a-f1c814044a3b',
      'seq_num': 0,
      'state': 'active',
      'time': 1461595260.575152,
      'uid': '320ed2f7-acd7-4966-b3d8-d3006b94a166'},
     {'sample': '249c51e1-ba7f-4412-834a-f1c814044a3b',
      'seq_num': 0,
      'state': 'active',
      'time': 1461349983.847516,
      'uid': '07675e66-4886-492f-851d-6110bd2ce910'},
     {'sample': '712b0feb-2667-4b22-aa8a-061ecf14af0a',
      'seq_num': 0,
      'state': 'active',
      'time': 1461349846.453589,
      'uid': 'e5bcc711-de1f-4ab4-b1d1-5f2a56e411a3'},
     {'antihero': 'romans',
      'foo': 'bar',
      'hero': 'obelix',
      'sample': 'NULL',
      'seq_num': 0,
      'state': 'inactive',
      'time': 1461331980.517245,
      'uid': '8122e975-4cfe-4afe-9d06-dffbe674796c'},
     {'antihero': 'romans',
      'foo': 'bar',
      'hero': 'obelix',
      'sample': 'NULL',
      'seq_num': 0,
      'state': 'active',
      'time': 1461331979.489911,
      'uid': '7f92cff1-9455-49f0-addd-dee9a82d42a0'},
     {'antihero': 'romans',
      'foo': 'bar',
      'hero': 'asterix',
      'sample': 'NULL',
      'seq_num': 0,
      'state': 'active',
      'time': 1461331978.460395,
      'uid': 'efb60a85-b730-40bc-8f86-46f99a7b8fac'},
     {'antihero': 'romans',
      'foo': 'bar',
      'hero': 'asterix',
      'sample': 'NULL',
      'seq_num': 0,
      'state': 'active',
      'time': 1461331977.438713,
      'uid': 'c01a998e-7c31-4d8e-9ec2-7651800137d9'},
     {'sample': 'NULL',
      'seq_num': 0,
      'state': 'active',
      'time': 1461331977.427048,
      'uid': '5e181a1e-f507-4ce7-9233-3f3eddc9caa1'},
     {'sample': 'NULL',
      'seq_num': 0,
      'state': 'active',
      'time': 1461331976.407339,
      'uid': '02248364-4beb-485d-b735-5258052b913b'}]



.. code:: python

    # Set the state of all requests for a given sample to 'inactive'
    conn3.update({'sample': '5a117ba4-ad8f-4716-a2ae-72d11acfb91d'}, {'state': 'inactive'})




.. parsed-literal::

    True



Local Sample Management Examples
================================

.. code:: python

    from amostra.client.local_commands import LocalSampleReference, LocalContainerReference, LocalRequestReference
    cnn = LocalSampleReference()
    cnn.create(name='b')




.. parsed-literal::

    {'container': 'NULL',
     'name': 'b',
     'time': 1461595544.629661,
     'uid': 'f5b10597-5952-4d14-ac95-1aa3c85ca198'}



.. code:: python

    list(cnn.find())




.. parsed-literal::

    [{'container': 'NULL',
      'name': 'minetoo',
      'time': 1461332863.319112,
      'uid': 'cbdb18e6-0b6a-489a-8e8b-0fb8c66021eb'},
     {'container': 'NULL',
      'name': 'minetoo',
      'time': 1461332881.641423,
      'uid': '6b906b24-6e46-4b3a-ace4-dcd2b804b1b9'},
     {'container': 'NULL',
      'name': 'minetoo',
      'time': 1461349847.362067,
      'uid': 'd7bb7d10-9c65-4ccd-a594-dc50258f8804'},
     {'container': 'NULL',
      'name': 'minetoo',
      'time': 1461349985.442712,
      'uid': '14676391-d1a2-44d4-96f7-832815a412e7'},
     {'container': 'NULL',
      'name': 'b',
      'time': 1461595515.105916,
      'uid': 'fbf9f1a3-c02c-449f-a208-67ec9edac803'},
     {'container': 'NULL',
      'name': 'b',
      'time': 1461595544.629661,
      'uid': 'f5b10597-5952-4d14-ac95-1aa3c85ca198'}]



.. code:: python

    cnn.update({'name': 'b'}, {'name': 'minetoo'})


.. parsed-literal::

    /Users/arkilic/amostra_files/samples.json {'name': 'b'} {'name': 'minetoo'}


.. code:: python

    conn_cont = LocalContainerReference()
    conn_cont.create()
    list(conn_cont.find(**{'uid': '3d2fdd7a-845b-4335-8b88-e6f5658e3e18'}))




.. parsed-literal::

    [{'container': 'NULL',
      'time': 1461331188.602469,
      'uid': '3d2fdd7a-845b-4335-8b88-e6f5658e3e18'}]


