from orator.migrations import Migration


class CreateTransTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('trans') as table:
            table.increments('id')
            table.string('name', 100).unique()
            table.string('type', 100).unique()
            table.timestamps()

        with self.schema.create('entries_trans') as table:
            table.increments('id')
            table.integer('tran_id').unsigned()
            table.foreign('tran_id').references('id').on('trans').on_delete('cascade')
            table.integer('entry_id').unsigned()
            table.foreign('entry_id').references('id').on('entries').on_delete('cascade')
            table.string('result', 100)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('trans')
        self.schema.drop('entries_trans')
